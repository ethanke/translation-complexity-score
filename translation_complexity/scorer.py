"""
Main interface for translation complexity scoring.
"""
from typing import Dict, List, Optional, Union

import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
import spacy
import nltk
from textstat import textstat

from .metrics.readability import ReadabilityMetrics
from .metrics.linguistic import LinguisticMetrics
from .metrics.translation import TranslationMetrics
from .config import Config

class TranslationComplexityScorer:
    """Main class for scoring translation complexity using multiple metrics."""
    
    def __init__(self, config: Optional[Config] = None):
        """Initialize the scorer with optional configuration."""
        self.config = config or Config()
        self._initialize_models()
        self.readability_metrics = ReadabilityMetrics()
        self.linguistic_metrics = LinguisticMetrics(self.nlp)
        self.translation_metrics = TranslationMetrics(self.tokenizer, self.model)
        
    def _initialize_models(self) -> None:
        """Initialize required NLP models and tokenizers."""
        # Initialize spaCy
        self.nlp = spacy.load("en_core_web_sm")
        
        # Initialize transformer model for embeddings
        self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        self.model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        
        # Move model to GPU if available
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")
            
    def score_text(self, text: str) -> Dict[str, float]:
        """
        Score the complexity of the given text using multiple metrics.
        
        Args:
            text: The text to analyze
            
        Returns:
            Dictionary containing various complexity scores
        """
        scores = {}
        
        # Get readability scores
        readability_scores = self.readability_metrics.score(text)
        scores.update(readability_scores)
        
        # Get linguistic feature scores
        linguistic_scores = self.linguistic_metrics.score(text)
        scores.update(linguistic_scores)
        
        # Get translation-specific scores
        translation_scores = self.translation_metrics.score(text)
        scores.update(translation_scores)
        
        # Calculate overall complexity score (weighted average)
        scores["overall_complexity"] = self._calculate_overall_score(
            readability_scores,
            linguistic_scores,
            translation_scores
        )
        
        return scores
    
    def _calculate_overall_score(
        self,
        readability_scores: Dict[str, float],
        linguistic_scores: Dict[str, float],
        translation_scores: Dict[str, float]
    ) -> float:
        """Calculate weighted average of all scores."""
        weights = self.config.get_metric_weights()
        
        # Calculate average for each category
        readability_avg = np.mean(list(readability_scores.values()))
        linguistic_avg = np.mean(list(linguistic_scores.values()))
        translation_avg = np.mean(list(translation_scores.values()))
        
        # Calculate weighted average across categories
        category_scores = np.array([readability_avg, linguistic_avg, translation_avg])
        category_weights = np.array([
            weights["readability"],
            weights["linguistic"],
            weights["translation"]
        ])
        
        # Ensure the score is between 0 and 1
        return float(np.clip(np.average(category_scores, weights=category_weights), 0, 1))
    
    def batch_score(self, texts: List[str]) -> List[Dict[str, float]]:
        """
        Score multiple texts in batch.
        
        Args:
            texts: List of texts to analyze
            
        Returns:
            List of dictionaries containing complexity scores
        """
        return [self.score_text(text) for text in texts] 
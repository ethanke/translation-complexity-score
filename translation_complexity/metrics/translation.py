"""
Translation-specific complexity metrics.
"""
from typing import Dict
import torch
from transformers import AutoTokenizer, AutoModel

class TranslationMetrics:
    """Class for analyzing translation-specific complexity."""
    
    def __init__(self, tokenizer: AutoTokenizer, model: AutoModel):
        """
        Initialize the translation metrics analyzer.
        
        Args:
            tokenizer: HuggingFace tokenizer
            model: HuggingFace model for embeddings
        """
        self.tokenizer = tokenizer
        self.model = model
    
    def score(self, text: str) -> Dict[str, float]:
        """
        Calculate translation-specific complexity scores.
        
        Args:
            text: The text to analyze
            
        Returns:
            Dictionary containing different translation complexity scores
        """
        scores = {}
        
        # Semantic complexity using embeddings
        scores["semantic_complexity"] = self._calculate_semantic_complexity(text)
        
        # Idiomatic density
        scores["idiomatic_density"] = self._calculate_idiomatic_density(text)
        
        # Domain specificity
        scores["domain_specificity"] = self._calculate_domain_specificity(text)
        
        return scores
    
    def _calculate_semantic_complexity(self, text: str) -> float:
        """Calculate semantic complexity using sentence embeddings."""
        # Tokenize and get model outputs
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Get sentence embedding
        embeddings = outputs.last_hidden_state.mean(dim=1)
        
        # Calculate complexity as distance from origin
        # (more complex sentences tend to have more distant embeddings)
        complexity = torch.norm(embeddings, dim=1).mean().item()
        
        # Normalize to 0-1 range
        return min(complexity / 10.0, 1.0)
    
    def _calculate_idiomatic_density(self, text: str) -> float:
        """Calculate the density of idiomatic expressions."""
        # This is a simplified version - in practice, you'd want to use
        # a comprehensive dictionary of idioms
        common_idioms = {
            "kick the bucket", "raining cats and dogs", "piece of cake",
            "let the cat out of the bag", "hit the nail on the head"
        }
        
        words = text.lower().split()
        if not words:
            return 0.0
            
        # Count occurrences of idioms
        idiom_count = 0
        for i in range(len(words) - 2):
            phrase = " ".join(words[i:i+3])
            if phrase in common_idioms:
                idiom_count += 1
        
        return min(idiom_count / (len(words) / 3), 1.0)
    
    def _calculate_domain_specificity(self, text: str) -> float:
        """Calculate domain-specific terminology density."""
        # This is a simplified version - in practice, you'd want to use
        # domain-specific terminology lists
        common_terms = {
            "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
            "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
            "this", "but", "his", "by", "from", "they", "we", "say", "her", "she"
        }
        
        words = text.lower().split()
        if not words:
            return 0.0
            
        # Count domain-specific terms (words not in common terms)
        domain_terms = [w for w in words if w not in common_terms]
        return len(domain_terms) / len(words) 
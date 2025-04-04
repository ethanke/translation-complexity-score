"""
Linguistic feature analysis for text complexity.
"""
from typing import Dict, List
import spacy
from spacy.tokens import Doc

class LinguisticMetrics:
    """Class for analyzing linguistic features of text."""
    
    def __init__(self, nlp: spacy.language.Language):
        """
        Initialize the linguistic metrics analyzer.
        
        Args:
            nlp: spaCy language model
        """
        self.nlp = nlp
    
    def score(self, text: str) -> Dict[str, float]:
        """
        Calculate various linguistic complexity scores.
        
        Args:
            text: The text to analyze
            
        Returns:
            Dictionary containing different linguistic complexity scores
        """
        doc = self.nlp(text)
        scores = {}
        
        # Calculate raw scores
        raw_scores = {
            "avg_sentence_length": self._calculate_avg_sentence_length(doc),
            "lexical_diversity": self._calculate_lexical_diversity(doc),
            "syntactic_complexity": self._calculate_syntactic_complexity(doc),
            "vocabulary_rarity": self._calculate_vocabulary_rarity(doc)
        }
        
        # Normalize scores to 0-1 range with more balanced thresholds
        scores["avg_sentence_length"] = min(raw_scores["avg_sentence_length"] / 30.0, 1.0)  # Increased threshold
        scores["lexical_diversity"] = raw_scores["lexical_diversity"] * 0.6  # Scaled down more
        scores["syntactic_complexity"] = min(raw_scores["syntactic_complexity"] / 10.0, 1.0)  # Increased threshold
        scores["vocabulary_rarity"] = raw_scores["vocabulary_rarity"] * 0.5  # Scaled down more
        
        return scores
    
    def _calculate_avg_sentence_length(self, doc: Doc) -> float:
        """Calculate average sentence length."""
        if not doc.sents:
            return 0.0
        return sum(len(sent) for sent in doc.sents) / len(list(doc.sents))
    
    def _calculate_lexical_diversity(self, doc: Doc) -> float:
        """Calculate type-token ratio."""
        tokens = [token.text.lower() for token in doc if not token.is_punct]
        if not tokens:
            return 0.0
        return len(set(tokens)) / len(tokens)
    
    def _calculate_syntactic_complexity(self, doc: Doc) -> float:
        """Calculate syntactic complexity based on dependency tree depth."""
        if not doc.sents:
            return 0.0
        
        depths = []
        for sent in doc.sents:
            # Calculate maximum depth of dependency tree
            max_depth = 0
            for token in sent:
                depth = 0
                current = token
                while current.head != current:
                    depth += 1
                    current = current.head
                max_depth = max(max_depth, depth)
            depths.append(max_depth)
        
        return sum(depths) / len(depths)
    
    def _calculate_vocabulary_rarity(self, doc: Doc) -> float:
        """Calculate vocabulary rarity based on word frequency."""
        # This is a simplified version - in practice, you'd want to use
        # a more comprehensive frequency list
        common_words = {
            "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
            "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
            "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
            "or", "an", "will", "my", "one", "all", "would", "there", "their",
            "what", "so", "up", "out", "if", "about", "who", "get", "which", "go",
            "me", "when", "make", "can", "like", "time", "no", "just", "him", "know",
            "take", "people", "into", "year", "your", "good", "some", "could", "them",
            "see", "other", "than", "then", "now", "look", "only", "come", "its",
            "over", "think", "also", "back", "after", "use", "two", "how", "our",
            "work", "first", "well", "way", "even", "new", "want", "because", "any",
            "these", "give", "day", "most", "us"
        }
        
        words = [token.text.lower() for token in doc if not token.is_punct]
        if not words:
            return 0.0
            
        rare_words = [w for w in words if w not in common_words]
        return len(rare_words) / len(words) 
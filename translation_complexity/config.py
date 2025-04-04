"""
Configuration settings for the translation complexity scorer.
"""
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    """Configuration class for the translation complexity scorer."""
    
    # Weights for different metric categories
    READABILITY_WEIGHT: float = 0.3
    LINGUISTIC_WEIGHT: float = 0.4
    TRANSLATION_WEIGHT: float = 0.3
    
    # Model settings
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    SPACY_MODEL: str = "en_core_web_sm"
    
    # Thresholds for complexity levels (adjusted for normalized scores)
    LOW_COMPLEXITY_THRESHOLD: float = 0.25  # Increased to better handle simple text
    MEDIUM_COMPLEXITY_THRESHOLD: float = 0.45  # Adjusted for better distribution
    HIGH_COMPLEXITY_THRESHOLD: float = 0.65  # Adjusted for better distribution
    
    def get_metric_weights(self) -> Dict[str, float]:
        """Get weights for different metric categories."""
        return {
            "readability": self.READABILITY_WEIGHT,
            "linguistic": self.LINGUISTIC_WEIGHT,
            "translation": self.TRANSLATION_WEIGHT,
        }
    
    def get_complexity_level(self, score: float) -> str:
        """Get complexity level based on score."""
        if score < self.LOW_COMPLEXITY_THRESHOLD:
            return "low"
        elif score < self.MEDIUM_COMPLEXITY_THRESHOLD:
            return "medium"
        elif score < self.HIGH_COMPLEXITY_THRESHOLD:
            return "high"
        else:
            return "very_high" 
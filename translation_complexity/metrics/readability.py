"""
Traditional readability metrics implementation.
"""
from typing import Dict
import textstat

class ReadabilityMetrics:
    """Class implementing traditional readability metrics."""
    
    def __init__(self):
        """Initialize the readability metrics calculator."""
        pass
    
    def score(self, text: str) -> Dict[str, float]:
        """
        Calculate various readability scores for the given text.
        
        Args:
            text: The text to analyze
            
        Returns:
            Dictionary containing different readability scores
        """
        try:
            scores = {}
            
            # Flesch-Kincaid Grade Level (typically 0-20)
            scores["flesch_kincaid"] = max(0, min(20, textstat.flesch_kincaid_grade(text)))
            
            # Coleman-Liau Index (typically 0-20)
            scores["coleman_liau"] = max(0, min(20, textstat.coleman_liau_index(text)))
            
            # Gunning Fog Index (typically 0-20)
            scores["gunning_fog"] = max(0, min(20, textstat.gunning_fog(text)))
            
            # SMOG Index (typically 0-20)
            scores["smog"] = max(0, min(20, textstat.smog_index(text)))
            
            # Flesch Reading Ease (typically 0-100)
            scores["flesch_reading_ease"] = max(0, min(100, textstat.flesch_reading_ease(text)))
            
            # Normalize scores to 0-1 range with more lenient thresholds
            normalized_scores = {}
            for metric, score in scores.items():
                if metric == "flesch_reading_ease":
                    # Invert Flesch Reading Ease (higher score = lower complexity)
                    # More lenient threshold for simple text
                    normalized_scores[metric] = 1.0 - (score / 120.0)  # Increased threshold
                else:
                    # For grade level metrics, normalize assuming max grade level of 25
                    # More lenient threshold for simple text
                    normalized_scores[metric] = score / 25.0  # Increased threshold
            
            return normalized_scores
            
        except Exception as e:
            print(f"Warning: Error calculating readability metrics: {str(e)}")
            return {
                "flesch_kincaid": 0.0,
                "coleman_liau": 0.0,
                "gunning_fog": 0.0,
                "smog": 0.0,
                "flesch_reading_ease": 0.0
            } 
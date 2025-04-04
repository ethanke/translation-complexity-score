"""
Comprehensive test cases for the Translation Complexity Scorer.
"""
from typing import Dict
import json
import time
from translation_complexity import TranslationComplexityScorer
from translation_complexity.config import Config

def format_scores(scores: Dict[str, float]) -> str:
    """Format scores for better readability."""
    return json.dumps(scores, indent=2)

def analyze_complexity(text: str, scorer: TranslationComplexityScorer) -> None:
    """Analyze and print detailed complexity scores for a given text."""
    try:
        print(f"\nAnalyzing text: '{text}'")
        print("-" * 80)
        
        start_time = time.time()
        scores = scorer.score_text(text)
        processing_time = time.time() - start_time
        
        print(f"\nProcessing time: {processing_time:.2f} seconds")
        print("\nDetailed Scores:")
        print(format_scores(scores))
        
        # Get complexity level
        complexity_level = scorer.config.get_complexity_level(scores["overall_complexity"])
        print(f"\nOverall Complexity Level: {complexity_level}")
        
        # Analyze individual components
        print("\nComponent Analysis:")
        print(f"Readability Score: {scores.get('flesch_reading_ease', 0):.2f}")
        print(f"Linguistic Complexity: {scores.get('syntactic_complexity', 0):.2f}")
        print(f"Translation Complexity: {scores.get('semantic_complexity', 0):.2f}")
        
    except Exception as e:
        print(f"Error analyzing text: {str(e)}")
        print("Skipping to next test case...")

def main():
    """Run comprehensive tests with various text examples."""
    try:
        print("Initializing Translation Complexity Scorer...")
        # Initialize scorer with custom config
        config = Config(
            READABILITY_WEIGHT=0.3,
            LINGUISTIC_WEIGHT=0.4,
            TRANSLATION_WEIGHT=0.3
        )
        scorer = TranslationComplexityScorer(config)
        print("Initialization complete!")
        
        # Test Case 1: Simple text
        print("\n" + "="*80)
        print("Test Case 1: Simple Text")
        print("="*80)
        simple_text = "The cat sat on the mat. It was a sunny day."
        analyze_complexity(simple_text, scorer)
        
        # Test Case 2: Complex technical text
        print("\n" + "="*80)
        print("Test Case 2: Technical Text")
        print("="*80)
        technical_text = """
        The quantum mechanical wave function describes the probability amplitude 
        of finding a particle in a particular state. When subjected to measurement, 
        the wave function collapses to an eigenstate of the observable being measured.
        """
        analyze_complexity(technical_text, scorer)
        
        # Test Case 3: Text with idioms
        print("\n" + "="*80)
        print("Test Case 3: Idiomatic Text")
        print("="*80)
        idiomatic_text = """
        It's raining cats and dogs outside, but I'm not going to let that get me down. 
        I'll hit the nail on the head with this project, even if it's a piece of cake.
        """
        analyze_complexity(idiomatic_text, scorer)
        
        # Test Case 4: Long complex sentence
        print("\n" + "="*80)
        print("Test Case 4: Complex Sentence")
        print("="*80)
        complex_sentence = """
        The intricate web of interconnected neural networks, which had been carefully 
        trained on vast datasets comprising millions of diverse examples, demonstrated 
        remarkable adaptability when confronted with novel scenarios that deviated 
        significantly from the patterns observed during the initial training phase.
        """
        analyze_complexity(complex_sentence, scorer)
        
        # Test Case 5: Batch processing
        print("\n" + "="*80)
        print("Test Case 5: Batch Processing")
        print("="*80)
        texts = [
            "The quick brown fox jumps over the lazy dog.",
            "In the realm of quantum mechanics, the uncertainty principle states that we cannot simultaneously know both the position and momentum of a particle with arbitrary precision.",
            "She hit the ground running and never looked back, making it to the finish line in record time."
        ]
        
        start_time = time.time()
        batch_scores = scorer.batch_score(texts)
        processing_time = time.time() - start_time
        
        print(f"\nBatch processing time: {processing_time:.2f} seconds")
        for i, (text, scores) in enumerate(zip(texts, batch_scores), 1):
            print(f"\nText {i}: '{text[:50]}...'")
            print(f"Overall Complexity: {scores['overall_complexity']:.2f}")
            print(f"Complexity Level: {scorer.config.get_complexity_level(scores['overall_complexity'])}")
        
        print("\nAll test cases completed successfully!")
        
    except Exception as e:
        print(f"\nError during test execution: {str(e)}")
        print("Test execution terminated.")

if __name__ == "__main__":
    main()
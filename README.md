# Translation Complexity Scorer

A tool for scoring translation complexity using multiple metrics and machine learning approaches. This tool helps translators, language service providers, and researchers assess text complexity to optimize translation workflows and resource allocation.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

### Multiple Scoring Methods
- **Traditional Readability Metrics**
  - Flesch-Kincaid Grade Level
  - Coleman-Liau Index
  - Gunning Fog Index
  - SMOG Index
  - Flesch Reading Ease

- **Linguistic Feature Analysis**
  - Average sentence length
  - Lexical diversity (Type-Token Ratio)
  - Syntactic complexity (Dependency tree depth)
  - Vocabulary rarity analysis

- **Translation-Specific Metrics**
  - Semantic complexity using transformer embeddings
  - Idiomatic expression density
  - Domain-specific terminology detection

### Technical Highlights
- 🚀 GPU acceleration support (CUDA compatible)
- 📊 Normalized scores (0-1 range)
- 🎯 Configurable weights for different metrics
- 📈 Batch processing support
- 🔍 Detailed score breakdown
- 🧪 Comprehensive test suite

## 📋 Requirements

- Python 3.8+
- CUDA-compatible GPU (optional, for faster processing)
- 4GB+ RAM

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/ethanke/translation-complexity-score.git
cd translation-complexity-score

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download required models
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt averaged_perceptron_tagger
```

## 🚀 Quick Start

```python
from translation_complexity import TranslationComplexityScorer

# Initialize the scorer
scorer = TranslationComplexityScorer()

# Score a single text
text = "Your text to analyze here."
scores = scorer.score_text(text)

print(f"Overall Complexity: {scores['overall_complexity']:.2f}")
print(f"Complexity Level: {scorer.config.get_complexity_level(scores['overall_complexity'])}")

# Batch processing
texts = ["Text 1", "Text 2", "Text 3"]
batch_scores = scorer.batch_score(texts)
```

## 📊 Example Output

```json
{
  "flesch_kincaid": 0.45,
  "coleman_liau": 0.38,
  "gunning_fog": 0.52,
  "smog": 0.41,
  "flesch_reading_ease": 0.65,
  "avg_sentence_length": 0.48,
  "lexical_diversity": 0.72,
  "syntactic_complexity": 0.55,
  "vocabulary_rarity": 0.33,
  "semantic_complexity": 0.61,
  "idiomatic_density": 0.25,
  "domain_specificity": 0.44,
  "overall_complexity": 0.48
}
```

## 🏗️ Project Structure

```
translation_complexity/
├── metrics/
│   ├── readability.py    # Traditional readability metrics
│   ├── linguistic.py     # Linguistic feature analysis
│   └── translation.py    # Translation-specific metrics
├── utils/
│   └── helpers.py        # Utility functions
├── config.py             # Configuration settings
└── scorer.py            # Main scoring interface
```

## ⚙️ Configuration

You can customize the scoring weights and thresholds:

```python
from translation_complexity import Config, TranslationComplexityScorer

config = Config(
    READABILITY_WEIGHT=0.3,
    LINGUISTIC_WEIGHT=0.4,
    TRANSLATION_WEIGHT=0.3,
    LOW_COMPLEXITY_THRESHOLD=0.25,
    MEDIUM_COMPLEXITY_THRESHOLD=0.45,
    HIGH_COMPLEXITY_THRESHOLD=0.65
)

scorer = TranslationComplexityScorer(config)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Citation

If you use this tool in your research, please cite:

```bibtex
@software{translation_complexity_scorer,
  title = {Translation Complexity Scorer},
  author = {Ethan Kerdelhue},
  year = {2025},
  url = {https://github.com/ethanke/translation-complexity-score}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the Hugging Face team for their transformer models
- spaCy team for their excellent NLP library
- NLTK contributors for their linguistic analysis tools 

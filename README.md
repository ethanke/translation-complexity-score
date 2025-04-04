# Translation Complexity Scorer

A tool for scoring translation complexity using multiple metrics and approaches.

## Features

- Multiple complexity scoring methods:
  - Traditional readability metrics (Flesch-Kincaid, Coleman-Liau, etc.)
  - Linguistic feature analysis
  - NLP-based complexity scoring
  - Translation-specific complexity metrics
- Modular architecture for easy extension
- Comprehensive test suite
- Type hints and documentation

## Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt averaged_perceptron_tagger
```

## Usage

```python
from translation_complexity import TranslationComplexityScorer

scorer = TranslationComplexityScorer()
score = scorer.score_text("Your text here")
print(f"Complexity score: {score}")
```

## Project Structure

- `translation_complexity/`: Main package directory
  - `metrics/`: Different complexity scoring methods
  - `utils/`: Helper functions and utilities
  - `models/`: ML models and embeddings
  - `config.py`: Configuration settings
  - `scorer.py`: Main scoring interface

## Development

```bash
# Run tests
pytest

# Format code
black .
isort .

# Type checking
mypy .
```

## License

MIT License 
# Testing Quick Reference

Quick reference for running tests in the awesome-python repository.

## Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=sort --cov-report=term-missing

# Run specific test file
pytest tests/test_sort.py

# Run specific test
pytest tests/test_sort.py::TestMain::test_main_sorts_links_alphabetically

# Run tests matching pattern
pytest tests/ -k "alphabetically"
```

## Using Make Commands

```bash
# Install all dependencies
make dev_install

# Run tests
make test

# Run tests with coverage (generates HTML report)
make test_coverage
```

## Test Structure

```
tests/
├── __init__.py
└── test_sort.py    # Tests for sort.py module
```

## Writing a New Test

```python
def test_your_feature(self, tmp_path):
    """Test description goes here."""
    # Arrange: Set up test data
    test_data = create_data()
    
    # Act: Execute function
    result = your_function(test_data)
    
    # Assert: Verify result
    assert result == expected_value
```

## Current Test Coverage

- **11 test cases** covering sort.py functionality
- **95% code coverage**
- Tests include:
  - Basic sorting functionality
  - Multiple sections handling
  - Edge cases (empty files, no links, special characters)
  - Case-insensitive sorting
  - Nested lists

## Before Submitting PR

```bash
# Ensure all tests pass
pytest tests/

# Check coverage
pytest tests/ --cov=sort --cov-report=term-missing

# Run the sort script
python sort.py
```

## CI/CD

Tests run automatically on Travis CI for every push. All tests must pass before merging.

## Need Help?

See [TDD_GUIDE.md](TDD_GUIDE.md) for comprehensive testing guide.

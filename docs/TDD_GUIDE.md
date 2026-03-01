# Test-Driven Development Guide

## Overview

This repository follows Test-Driven Development (TDD) practices to ensure code quality, reliability, and maintainability. This guide explains the TDD approach and how to apply it when contributing to this project.

## What is TDD?

Test-Driven Development (TDD) is a software development approach where tests are written before the actual code. The TDD cycle consists of three phases:

1. **Red**: Write a failing test that defines the desired functionality
2. **Green**: Write the minimum code necessary to make the test pass
3. **Refactor**: Improve the code while keeping all tests passing

## The TDD Cycle

### 1. Red Phase - Write a Failing Test

Start by writing a test that describes what you want your code to do. This test should fail initially because the functionality doesn't exist yet.

```python
def test_new_feature(self):
    """Test the new feature we want to add."""
    result = new_function(input_data)
    assert result == expected_output
```

### 2. Green Phase - Make the Test Pass

Write just enough code to make your test pass. Don't worry about perfection at this stage.

```python
def new_function(input_data):
    # Minimal implementation to pass the test
    return expected_output
```

### 3. Refactor Phase - Improve the Code

Now that your test is passing, refactor your code to improve its quality, readability, and maintainability. Your tests will ensure you don't break functionality during refactoring.

## Benefits of TDD

- **Better Design**: Writing tests first forces you to think about the API and design before implementation
- **Documentation**: Tests serve as living documentation of how the code should behave
- **Confidence**: A comprehensive test suite gives you confidence to refactor and make changes
- **Fewer Bugs**: Catching issues early in the development cycle reduces bugs in production
- **Faster Development**: While it may seem slower initially, TDD often speeds up development by reducing debugging time

## TDD Best Practices

### 1. Write Small, Focused Tests

Each test should verify one specific behavior:

```python
# Good: Tests one specific behavior
def test_sorts_alphabetically_case_insensitive(self):
    result = sort_items(['Zebra', 'alpha', 'Beta'])
    assert result == ['alpha', 'Beta', 'Zebra']

# Avoid: Tests multiple behaviors
def test_sorting_and_filtering(self):
    # Tests too many things at once
    ...
```

### 2. Use Descriptive Test Names

Test names should clearly describe what is being tested:

```python
# Good: Clear description
def test_main_sorts_links_alphabetically(self):
    ...

# Avoid: Unclear description
def test_main_works(self):
    ...
```

### 3. Follow the AAA Pattern

Structure tests using Arrange-Act-Assert:

```python
def test_example(self):
    # Arrange: Set up test data and conditions
    input_data = create_test_data()
    
    # Act: Execute the function being tested
    result = function_under_test(input_data)
    
    # Assert: Verify the result
    assert result == expected_value
```

### 4. Test Edge Cases

Don't just test the happy path. Consider edge cases:

```python
def test_empty_input(self):
    """Test handling of empty input."""
    result = process_data([])
    assert result == []

def test_single_item(self):
    """Test handling of single item."""
    result = process_data(['item'])
    assert result == ['item']

def test_special_characters(self):
    """Test handling of special characters."""
    result = process_data(['item-1', 'item.2', 'item_3'])
    # Assert expected behavior
```

### 5. Keep Tests Independent

Each test should be independent and not rely on the state from other tests:

```python
# Good: Each test sets up its own data
def test_feature_a(self, tmp_path):
    data = create_test_data()
    # Test feature A
    
def test_feature_b(self, tmp_path):
    data = create_test_data()
    # Test feature B
```

## Running Tests

### Install Dependencies

```bash
pip install -r requirements-dev.txt
```

### Run All Tests

```bash
pytest tests/
```

or using make:

```bash
make test
```

### Run with Coverage

```bash
pytest tests/ --cov=sort --cov-report=term-missing
```

or:

```bash
make test_coverage
```

### Run Specific Tests

```bash
# Run a specific test file
pytest tests/test_sort.py

# Run a specific test class
pytest tests/test_sort.py::TestMain

# Run a specific test method
pytest tests/test_sort.py::TestMain::test_main_sorts_links_alphabetically

# Run tests matching a pattern
pytest tests/ -k "sort"
```

## Example: Adding a New Feature Using TDD

Let's walk through adding a hypothetical new feature using TDD.

### Scenario: Add validation for link format

#### Step 1: Write the Test First (Red)

```python
def test_validates_link_format(self):
    """Test that invalid link format is detected."""
    invalid_links = [
        "* Zebra - Missing URL",
        "* [Zebra] - Missing URL parentheses"
    ]
    
    for link in invalid_links:
        result = validate_link_format(link)
        assert result is False, f"Should reject: {link}"
    
    valid_link = "* [Zebra](http://example.com) - Description."
    assert validate_link_format(valid_link) is True
```

Run the test and watch it fail:
```bash
pytest tests/test_sort.py::TestNewFeature::test_validates_link_format
```

#### Step 2: Implement the Feature (Green)

```python
import re

def validate_link_format(link):
    """Validate that a link follows the expected format."""
    pattern = r'\* \[.+\]\(.+\) - .+\.'
    return bool(re.match(pattern, link))
```

Run the test again:
```bash
pytest tests/test_sort.py::TestNewFeature::test_validates_link_format
```

The test should now pass!

#### Step 3: Refactor (if needed)

Review your code and refactor for clarity, performance, or maintainability. Your test will ensure the functionality remains correct.

## Continuous Integration

Tests run automatically on every push via Travis CI. The CI pipeline:

1. Installs dependencies
2. Runs all tests with coverage
3. Runs the sort script
4. Builds the documentation site

Make sure all tests pass before submitting a pull request!

## Common Testing Patterns

### Using Fixtures

Pytest fixtures help set up test data:

```python
import pytest

@pytest.fixture
def sample_readme(tmp_path):
    """Create a sample README for testing."""
    content = """# Awesome Python
- - -
## Libraries
* [Zebra](http://example.com) - Description.
* [Alpha](http://example.com) - Description.
"""
    readme_file = tmp_path / "README.md"
    readme_file.write_text(content)
    return readme_file
```

### Temporary Directories

Use `tmp_path` fixture for file operations:

```python
def test_file_operations(self, tmp_path):
    """Test with temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    # Test operations...
```

### Testing Exceptions

Test error handling:

```python
def test_raises_error_on_invalid_input(self):
    """Test that appropriate error is raised."""
    with pytest.raises(ValueError, match="Invalid input"):
        function_that_should_raise("invalid")
```

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Test Driven Development: By Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530) by Kent Beck
- [Python Testing with pytest](https://pragprog.com/titles/bopytest/python-testing-with-pytest/) by Brian Okken

## Questions?

If you have questions about TDD practices in this project, please:

1. Check the existing tests in `tests/` for examples
2. Review this guide
3. Open an issue for discussion
4. Ask in your pull request

Happy testing!

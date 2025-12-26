# Contributing

Your contributions are always welcome!

## Test-Driven Development (TDD)

This project follows Test-Driven Development practices. When contributing code changes:

1. **Write tests first**: Before implementing new features or fixing bugs, write tests that describe the expected behavior.
2. **Run tests**: Execute the test suite to verify your tests fail initially (Red phase).
3. **Implement code**: Write the minimum code necessary to make your tests pass (Green phase).
4. **Refactor**: Improve code quality while ensuring all tests still pass (Refactor phase).
5. **Submit with tests**: All pull requests with code changes must include corresponding tests.

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest tests/

# Run tests with coverage
pytest tests/ --cov=sort --cov-report=term-missing
```

## Guidelines

* Add one link per Pull Request.
    * Make sure the PR title is in the format of `Add project-name`.
    * Write down the reason why the library is awesome.
* Add the link: `* [project-name](http://example.com/) - A short description ends with a period.`
    * Keep descriptions concise and **short**.
* Add a section if needed.
    * Add the section description.
    * Add the section title to Table of Contents.
* Search previous Pull Requests or Issues before making a new one, as yours may be a duplicate.
* Don't mention `Python` in the description as it's implied.
* Check your spelling and grammar.
* Remove any trailing whitespace.

Just a gentle reminder: **Try not to submit your own project. Instead, wait for someone finds it useful and submits it for you.**

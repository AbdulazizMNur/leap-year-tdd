# Leap Year TDD Kata

A small Python kata demonstrating test-driven development against the Gregorian leap-year rules.

## Rules

A year is a leap year when:

1. it is divisible by 400; or
2. it is divisible by 4 but not by 100.

The boundary cases are the point of the exercise: 2024 is a leap year, 1900 is not, and 2000 is.

## Run the tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

GitHub Actions runs the same test suite for pull requests and pushes to `main`.

## Skills demonstrated

Python, test-driven development, boundary-value testing, pytest and continuous integration.

# Library Management System

A Python project used for the Agile Software Development Laboratory. It supports book registration/search and book issue/return operations.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -v
python -m pytest --cov=book --cov=library --cov-report=term-missing
```

## CI/CD

GitHub Actions workflow: `.github/workflows/ci-cd.yml`

The workflow runs automatically on every push and pull request to the repository's default branch. It prepares/builds the Python modules, runs the automated tests, performs Flake8 source analysis, and uploads test and coverage reports as workflow artifacts.
CI/CD pipeline verified successfully.

# Data Structures & Algorithms (Python)

This repository contains my implementations of classical data structures and algorithms in Python.
The goal of this project is to practice computer science fundamentals, clean code principles, and unit testing.

## 📂 Features

All implementations are fully typed (using `typing`) and tested with `pytest`.

### Data Structures
- [x] **Stack** (LIFO)
- [x] **Queue** (FIFO)
- [x] **Linked Lists** (Singly & Doubly)
- [x] **Hash Map** (with chaining for collisions)
- [x] **Binary Tree** (Binary Search Tree)

### Algorithms
- [x] **Binary Search** (Generic implementation)
- [x] **Recursion** (Factorial, Fibonacci, Sums)

---

## 🛠️ Development & Testing

This project maintains high code quality standards using strict linting, static type checking, and comprehensive testing via **Tox**.

### 1. Environment Setup

It is recommended to use a virtual environment for development to keep dependencies isolated.

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### 2. Running Tests (Quick Start)

To run unit tests directly using `pytest` (fastest method during active coding):

```bash
# Run all tests with verbose output
pytest -v

# Run a specific test module
pytest tests/test_stack.py
```

### 3. Automation with Tox (Recommended)

This project uses `tox` to automate the testing process in isolated environments. This ensures that the code works across different Python versions and passes all quality checks (linting, typing).

**Prerequisite:** Make sure you have compatible Python versions installed (3.10, 3.11, 3.12), or `tox` will skip missing interpreters.

```bash
# Run the full suite (Tests on all Py versions + Flake8 + MyPy)
tox

# Run only code quality checks (faster, no tests)
tox -e flake8,mypy

# Run tests against a specific Python version
tox -e py312
```

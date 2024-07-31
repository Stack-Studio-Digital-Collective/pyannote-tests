# Pyannote Test

Current state is just simple python code to test the pyannote library to compare performance on Mac + AMD gpu.

## Installation

```bash
poetry install
```

## Usage

```bash
poetry run python pyannote_test/main.py
```

## Results

Slow on Mac :( ~45-50% of the length of the clip for 3.0 version and closer to 90% of the length of the clip for 3.1 version.

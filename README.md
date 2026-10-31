![Python checks](https://github.com/leakquicked/filetype-detector/actions/workflows/python-checks.yml/badge.svg)

# Filetype Detector

Identify common file formats from leading signature bytes.

## Requirements
Python 3.10+, standard library only.

## Usage
`python filetype_detector.py --help`

Processes local files only; no network requests or uploads. Do not publish confidential inventories.

## Tests
`python -m unittest discover -s tests -v`

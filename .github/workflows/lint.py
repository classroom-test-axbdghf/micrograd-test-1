name: Lint

on:
  push:
    branches:
      - main/**


jobs:
  test_lint:
    name: Lint
    runs-on: ubuntu-22.04
    strategy:
      matrix:
        python-version: ['3.11']

    steps:
    - uses: actions/checkout@v3
      with:
        fetch-depth: 0
        submodules: recursive

    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install Python packages
      run: |
        python -m pip install ruff cython-lint

    - name: CheckTests
      run: |
        set -euo pipefail
        python -m pytest
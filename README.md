## Setup (uv)

This repo uses `uv` to manage the virtual environment and dependencies.

### Prerequisites

- Python **3.10+**
- `uv` installed

Install `uv` (pick one):

```bash
pipx install uv
```

or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install dependencies

From the repo root:

```bash
uv venv
uv sync
```

### Run tests

```bash
uv run pytest -q
```

## Add a new solution

### 1) Create the solution file

- Put solutions in: `solutions/`
- Naming convention: `sNNN_<problem_slug>.py` (example: `s037_some_problem.py`)
- Export a class named **`Solution`** (unless the file already uses `Solution1`, `Solution2`, etc.)
- Implement the LeetCode-style method on that class (example: `def twoSum(...)`)

### 2) Create the matching test file

- Put tests in: `tests/`
- Naming convention: `test_sNNN_<problem_slug>.py`
- Follow the same structure used by `tests/test_s001_valid_anagram.py`:
  - import `pytest`
  - import the solution class (example: `from ..solutions.s037_some_problem import Solution`)
  - define `TEST_CASES = [(inputs_dict, expected_output), ...]`
  - parametrize and assert

### 3) Run the test suite

```bash
uv run pytest -q
```


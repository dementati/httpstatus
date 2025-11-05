# httpstatus

Small CLI to print the name and a short description for an HTTP status code.

## Example

Run directly with the module:

```bash
python -m httpstatus 200
```

Or run the script after installing the package in editable mode:

```bash
# Using a virtual environment (recommended)
pip install -e .
httpstatus 404
```

## Using uv to manage venvs and deps

If you use `uv` to manage virtual environments and dependencies, the typical flow is:

1. Install `uv` (one-time):

```bash
pip install uv
```

2. Create or activate a venv with `uv` (exact subcommands depend on your `uv` version; if `uv` provides a venv command use it, otherwise fall back to `python -m venv .venv`):

```bash
# example (may vary by uv version)
uv venv create .venv
source .venv/bin/activate
# or on Windows (bash):
source .venv/Scripts/activate
```

3. Install project dependencies (editable):

```bash
pip install -e .
```

4. Run the CLI:

```bash
httpstatus 500
```

Note: If you don't have `uv` available, the steps above also work with the standard `python -m venv` workflow.

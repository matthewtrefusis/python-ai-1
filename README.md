# python-ai-1

`python-ai-1` is a small Python workspace built around two ideas:

1. a lightweight AI-powered command-line assistant that can decide when to use tools

It is intentionally compact and easy to explore. The codebase is useful as a learning project for function calling, safe file operations, and small CLI program design.



## What’s inside

- `main.py` starts the AI assistant CLI.
- `call_function.py` exposes the available tool schema to the model.
- `functions/` contains the safe file and execution helpers used by the exercises.
- `calculator/` contains a standalone expression evaluator and a small formatter for JSON output.
- `test_*.py` files and `calculator/tests.py` provide example-driven checks for the helper functions and calculator behavior.

## AI assistant CLI

The root-level `main.py` script sends a user prompt to Google’s GenAI API and prints the model’s response. It is configured to use a tool for listing files and directories, with paths restricted to the current working directory.

The script expects a `GEMINI_API_KEY` environment variable to be set.

Example:

```bash
python main.py "List the files in this project"
```

Use `--verbose` to print a little extra debug information about the request and token counts.

## File helper functions

The helper modules in `functions/` are designed to work safely inside a permitted working directory:

- `get_files_info.py` lists files in a directory.
- `get_file_content.py` reads the contents of a file.
- `write_file.py` writes text to a file.
- `run_python_file.py` executes a Python file and captures its output.

Each helper checks that paths stay within the allowed workspace boundary before doing anything else.

## Requirements

- Python 3.12+
- `google-genai`
- `python-dotenv`

The project metadata is defined in `pyproject.toml`.

## Installation

1. Create a virtual environment.

	```bash
	uv .venv
	```

2. Activate it.

	```bash
	source .venv/bin/activate
	```

3. Install the dependencies.

	```bash
	pip install google-genai==1.12.1 python-dotenv==1.1.0
	```

4. Set your Gemini API key in a .env file before running the AI assistant.

	```bash
	GEMINI_API_KEY="your-api-key-here"
	```

After that, you can run the scripts from the repository root.

## Project structure

```text
.
├── main.py
├── call_function.py
├── functions/
├── calculator/
├── test_get_file_content.py
├── test_get_files_info.py
├── test_run_python_file.py
└── test_write_file.py
```

## Notes

This repository is small on purpose, which makes it a good base for experimenting with agent tool calls, file safety checks, and simple CLI workflows.

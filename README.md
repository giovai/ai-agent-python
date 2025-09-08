# AI Coding Agent

A Python-based AI coding assistant that can interact with the file system and execute Python code within a secure sandboxed environment.

## Features

- List files and directories
- Read file contents
- Execute Python files with arguments
- Create and modify files
- Secure path handling to prevent directory traversal

## Prerequisites

- Python 3.8+
- A Gemini API key
- `uv` package manager (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-agent-python
   ```

2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the agent with a prompt:
```bash
uv run main.py "your prompt here" [--verbose]
```

### Examples

List files in the current directory:
```bash
uv run main.py "list files in the current directory"
```

Read a file:
```bash
uv run main.py "get the contents of lorem.txt"
```

Run a Python script:
```bash
uv run main.py "run tests.py"
```

Create or modify a file:
```bash
uv run main.py "create a new file.txt with contents 'Hello, World!'"
```

## Security

- All file operations are restricted to the working directory
- Path traversal attempts are blocked

## Project Structure

- `main.py` - Main entry point
- `config.py` - Configuration settings including working directory and max character limits
- `functions/` - Contains function implementations
  - `call_function.py` - Function dispatcher
  - `get_file_content.py` - File content reader
  - `get_files_info.py` - Directory lister
  - `run_python_file.py` - Python script executor
  - `write_file.py` - File writer
  - `common.py` - Shared utility functions
- `calculator/` - Example calculator application (default working directory)
- `tests.py` - Test suite

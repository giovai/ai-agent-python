import os
import subprocess
from google.genai import types

from functions.common import get_safe_full_path

def run_python_file(working_directory, file_path, args=[]):
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try: 
        full_path = get_safe_full_path(working_directory, file_path)

        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'

        result = subprocess.run(['python', file_path] + args, timeout=30, capture_output=True, cwd=(os.path.dirname(full_path)))

        result_string = ""
        if len(result.stdout) > 0:
            result_string += f'STDOUT: {result.stdout}\n'
        if len(result.stderr) > 0:
            result_string += f'STDERR: {result.stderr}\n'
        if not 0 == result.returncode:
            result_string += f'Process exited with code {result.returncode}'
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            result_string += "No output produced."

        return result_string

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the python file at the given path with optional arguments and prints its output with return code, constrained to the working directory and files with '.py' extension.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                default=[],
                items=types.Schema(type=types.Type.STRING),
                description="An optional list of arguments to use when executing the file.",
            ),
        },
    ),
)

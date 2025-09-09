import os
from google.genai import types

from utils.get_safe_file_path import get_safe_full_path

def write_file(working_directory, file_path, content):
    try:
        full_path = get_safe_full_path(working_directory, file_path)

        dir_name = os.path.dirname(full_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(full_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: failed to write file: {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a new file or overwrities an existing one, creates all missing directories in the file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write the contents to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file.",
            ),
        },
    ),
)

import os
from google.genai import types

from utils.get_safe_file_path import get_safe_full_path

def get_files_info(working_directory, directory="."):
    try:
        full_path = get_safe_full_path(working_directory, directory)

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        dir_entries = os.listdir(full_path)

        def get_dir_entry_info(entry):
            entry_path = f'{full_path}/{entry}'
            name = os.path.basename(entry_path)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)

            result = f'- {name}: file_size={size}, is_dir={is_dir}'
            return result

        files_info = map(get_dir_entry_info, dir_entries)
        return "\n".join(files_info)

    except Exception as e:
        return f'Error: failed to get files info: {e}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

import os
from functions.common import get_safe_full_path

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

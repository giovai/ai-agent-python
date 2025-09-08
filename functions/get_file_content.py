import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        joined_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(joined_path)
        
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" is not a file'


        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # check if reached the EOF
            if not "" == f.readline():
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

            return file_content_string

    except Exception as e:
        return f'Error: failed to get file contents: {e}'

import os

def get_safe_full_path(working_directory, path):
        joined_path = os.path.join(working_directory, path)
        full_path = os.path.abspath(joined_path)

        if not full_path.startswith(os.path.abspath(working_directory)):
            raise Exception(f'Error: Cannot access "{path}" as it is outside the permitted working directory')

        return full_path

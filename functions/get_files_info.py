import os

def get_files_info(working_directory, directory="."):
    try:
        joined_path = os.path.join(working_directory, directory)
        full_path = os.path.abspath(joined_path)

        if directory == ".":
            dir_name = "current"
        else:
            dir_name = f"\'{os.path.basename(full_path)}\'"

        if full_path.startswith(os.path.abspath(working_directory)) == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        dir_entries = os.listdir(full_path)
        header = f'Result for {dir_name} directory:\n'

        def get_dir_entry_info(entry):
            entry_path = f'{full_path}/{entry}'
            name = os.path.basename(entry_path)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)

            result = f'- {name}: file_size={size}, is_dir={is_dir}'
            return result

        files_info = map(get_dir_entry_info, dir_entries)
        return header + "\n".join(files_info)

    except Exception as e:
        return f'Error: failed to get files info: {e}'

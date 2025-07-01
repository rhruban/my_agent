import os


def get_files_info(working_directory, directory=None):
    full_working_dir = os.path.abspath(working_directory)
    target_dir = full_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(full_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            filesize = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            files_info.append(
                f"- {filename}: file_size={filesize} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return "Error: {e} while listing files"



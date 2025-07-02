import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    full_working_dir = os.path.abspath(working_directory)
    target_file = full_working_dir
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(full_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.' 
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python", target_file]
        if args:
            commands.extend(args)
        output = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=full_working_dir,
        )
        

        out_strings = []
        if output.stdout:
            out_strings.append(f"STDOUT:\n{output.stdout}")
        if output.stderr:
            out_strings.append(f"STDERR:\n{output.stderr}")

        if output.returncode != 0:
            out_strings.append(f"Proces exited with code {output.returncode}.")

        return "\n".join(out_strings) if out_strings else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"



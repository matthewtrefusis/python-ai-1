import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Ensure absolute_file_path is inside working_directory
        if os.path.commonpath([working_dir_abs, absolute_file_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not absolute_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]
        if args:
            command.extend(args)

        completed = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        parts = []
        if completed.returncode != 0:
            parts.append(f"Process exited with code {completed.returncode}")

        stdout = (completed.stdout or "").strip()
        stderr = (completed.stderr or "").strip()

        if stdout == "" and stderr == "":
            parts.append("No output produced")
        else:
            if stdout:
                parts.append(f"STDOUT:\n{stdout}")
            if stderr:
                parts.append(f"STDERR:\n{stderr}")

        return "\n".join(parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"

import os

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if valid_target_file == False:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return
    if os.path.isfile(target_file) == False:
        print(f'Error: File not found or is not a regular file: "{file_path}"') 
        return

    MAX_CHARS = 10000

    try:
        with open(target_file) as f:
            content = f.read(MAX_CHARS)
            if f.read(MAX_CHARS + 1) != "":
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except: 
        print("Error: Unable to read file")
    
    print(content)
    return content

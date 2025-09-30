import os

dir_path = "."  # current directory
entries = os.listdir(dir_path)
print("Files and Directories in current directory:")
for entry in entries:
    if os.path.isfile(entry):
        print(f"File: {entry}")
    else:
        print(f"Directory: {entry}")

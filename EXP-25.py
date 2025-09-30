import os

# -------------------------------
# File Operations (open, read, write, seek)
# -------------------------------

filename = "sample.txt"

# Create and write to file
with open(filename, "w") as f:
    f.write("Hello, Unix-like I/O\nSecond Line\nThird Line\n")
print(f"File '{filename}' created and written successfully.\n")

# Read the file
with open(filename, "r") as f:
    f.seek(0)  # Move cursor to beginning
    content = f.read()
print("File Content:")
print(content)

# File status (stat)
file_info = os.stat(filename)
print("File Information:")
print(f"Size: {file_info.st_size} bytes")
print(f"Created: {file_info.st_ctime}")
print(f"Last Modified: {file_info.st_mtime}\n")

# -------------------------------
# Directory Operations (opendir, readdir equivalent)
# -------------------------------

dir_path = "."  # current directory
print(f"Listing files in directory '{dir_path}':")
for entry in os.listdir(dir_path):
    entry_path = os.path.join(dir_path, entry)
    if os.path.isfile(entry_path):
        print(f"File: {entry}")
    elif os.path.isdir(entry_path):
        print(f"Directory: {entry}")

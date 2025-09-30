files = {}

def create(filename, content=""):
    if filename in files:
        print(f"{filename} already exists")
    else:
        files[filename] = content
        print(f"{filename} created")

def read(filename):
    print(files.get(filename, "File not found"))

def write(filename, content):
    if filename in files:
        files[filename] = content
        print(f"{filename} updated")
    else:
        print("File not found")

def delete(filename):
    if filename in files:
        del files[filename]
        print(f"{filename} deleted")
    else:
        print("File not found")

def list_files():
    print("Files:", list(files.keys()))

# Demo
create("file1.txt", "Hello")
write("file1.txt", "Updated")
read("file1.txt")
delete("file1.txt")
list_files()

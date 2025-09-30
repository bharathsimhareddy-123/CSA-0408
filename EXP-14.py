# single_level_directory.py

class SingleLevelDirectory:
    def __init__(self):
        self.files = {}  # Dictionary to store filename -> content

    def create(self, filename, content=""):
        if filename in self.files:
            print(f"File '{filename}' already exists.")
        else:
            self.files[filename] = content
            print(f"File '{filename}' created successfully.")

    def delete(self, filename):
        if filename in self.files:
            del self.files[filename]
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' not found.")

    def list_files(self):
        if self.files:
            print("Files in directory:", list(self.files.keys()))
        else:
            print("Directory is empty.")

    def read(self, filename):
        if filename in self.files:
            print(f"Content of '{filename}': {self.files[filename]}")
        else:
            print(f"File '{filename}' not found.")

    def write(self, filename, content):
        if filename in self.files:
            self.files[filename] = content
            print(f"File '{filename}' updated successfully.")
        else:
            print(f"File '{filename}' not found.")

# Demonstration
if __name__ == "__main__":
    dir = SingleLevelDirectory()

    # Creating files
    dir.create("file1.txt", "Hello World")
    dir.create("file2.txt", "Python Lab")

    # Listing files
    dir.list_files()

    # Reading files
    dir.read("file1.txt")

    # Writing/Updating file
    dir.write("file1.txt", "Updated Content")
    dir.read("file1.txt")

    # Deleting file
    dir.delete("file2.txt")
    dir.list_files()

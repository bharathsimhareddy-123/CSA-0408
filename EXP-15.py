# two_level_directory.py

class TwoLevelDirectory:
    def __init__(self):
        self.parent = {}  # parent_directory -> user_dir -> {filename: content}

    def create_user_dir(self, user_dir):
        if user_dir in self.parent:
            print(f"User directory '{user_dir}' already exists.")
        else:
            self.parent[user_dir] = {}
            print(f"User directory '{user_dir}' created successfully.")

    def create_file(self, user_dir, filename, content=""):
        if user_dir not in self.parent:
            print(f"User directory '{user_dir}' does not exist.")
        elif filename in self.parent[user_dir]:
            print(f"File '{filename}' already exists in '{user_dir}'.")
        else:
            self.parent[user_dir][filename] = content
            print(f"File '{filename}' created in '{user_dir}'.")

    def delete_file(self, user_dir, filename):
        if user_dir in self.parent and filename in self.parent[user_dir]:
            del self.parent[user_dir][filename]
            print(f"File '{filename}' deleted from '{user_dir}'.")
        else:
            print(f"File '{filename}' not found in '{user_dir}'.")

    def list_user_dirs(self):
        print("User Directories:", list(self.parent.keys()))

    def list_files(self, user_dir):
        if user_dir in self.parent:
            print(f"Files in '{user_dir}':", list(self.parent[user_dir].keys()))
        else:
            print(f"User directory '{user_dir}' does not exist.")

    def read_file(self, user_dir, filename):
        if user_dir in self.parent and filename in self.parent[user_dir]:
            print(f"Content of '{filename}' in '{user_dir}': {self.parent[user_dir][filename]}")
        else:
            print(f"File '{filename}' not found in '{user_dir}'.")

# Demonstration
if __name__ == "__main__":
    dir_system = TwoLevelDirectory()

    # Creating user directories
    dir_system.create_user_dir("userA")
    dir_system.create_user_dir("userB")

    # Creating files
    dir_system.create_file("userA", "doc1.txt", "Data for A1")
    dir_system.create_file("userA", "doc2.txt", "Data for A2")
    dir_system.create_file("userB", "report.txt", "Report for B")

    # Listing directories and files
    dir_system.list_user_dirs()
    dir_system.list_files("userA")
    dir_system.list_files("userB")

    # Reading a file
    dir_system.read_file("userA", "doc1.txt")

    # Deleting a file
    dir_system.delete_file("userA", "doc2.txt")
    dir_system.list_files("userA")

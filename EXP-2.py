import os
def copy_file(src, dst):
    src_fd = os.open(src, os.O_RDONLY)
    dst_fd = os.open(dst, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
    while True:
        data = os.read(src_fd, 1024)
        if not data:
            break
        os.write(dst_fd, data)  
    os.close(src_fd)
    os.close(dst_fd)
    print(f"Copied content from {src} to {dst}")
copy_file("C:/vscode/source.txt",
          "C:/vscode/destination.txt")
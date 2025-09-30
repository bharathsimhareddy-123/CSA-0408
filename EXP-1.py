import os
import multiprocessing
def child_process():
    print("Child Process:")
    print("  PID  =", os.getpid())
    print("  PPID =", os.getppid())
def main():
    process = multiprocessing.Process(target=child_process)
    process.start()
    print("Parent Process:")
    print("  PID  =", os.getpid())
    print("  PPID =", os.getppid())
    print("  Child PID =", process.pid)
    process.join()
if __name__ == "__main__":
    main()
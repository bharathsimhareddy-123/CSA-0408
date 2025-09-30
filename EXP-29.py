import threading
import time

def task(name):
    print(f"Thread {name} starting")
    time.sleep(1)
    print(f"Thread {name} exiting")

# Create threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

# Start threads
t1.start()
t2.start()

# Join threads
t1.join()
t2.join()

# Thread equality check
print("Are threads t1 and t2 the same?", t1 == t2)
print("Current thread:", threading.current_thread().name)

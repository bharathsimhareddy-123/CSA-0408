# mutex_synchronization.py

import threading
import time
import random

# Shared resource
counter = 0

# Mutex lock
mutex = threading.Lock()

# Function for threads to increment counter
def increment(thread_id, times=5):
    global counter
    for _ in range(times):
        mutex.acquire()  # enter critical section
        local_counter = counter
        print(f"Thread {thread_id} reads counter: {local_counter}")
        local_counter += 1
        time.sleep(random.uniform(0.1, 0.3))  # simulate processing
        counter = local_counter
        print(f"Thread {thread_id} updates counter to: {counter}")
        mutex.release()  # exit critical section
        time.sleep(random.uniform(0.1, 0.3))

if __name__ == "__main__":
    threads = []

    # Create 3 threads
    for i in range(3):
        t = threading.Thread(target=increment, args=(i, 5))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print(f"Final counter value: {counter}")

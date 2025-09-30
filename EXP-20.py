# reader_writer.py

import threading
import time
import random

# Shared resource
shared_data = 0
read_count = 0

# Semaphores
mutex = threading.Semaphore(1)       # protects read_count
rw_mutex = threading.Semaphore(1)    # exclusive access for writers

# Reader function
def reader(id, rounds=3):
    global read_count, shared_data
    for _ in range(rounds):
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            rw_mutex.acquire()  # first reader locks writers
        mutex.release()

        # Reading
        print(f"Reader {id} is reading value: {shared_data}")
        time.sleep(random.uniform(0.1, 0.5))

        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            rw_mutex.release()  # last reader unlocks writers
        mutex.release()
        time.sleep(random.uniform(0.1, 0.5))

# Writer function
def writer(id, rounds=3):
    global shared_data
    for _ in range(rounds):
        rw_mutex.acquire()
        shared_data += 1
        print(f"Writer {id} updated value to: {shared_data}")
        time.sleep(random.uniform(0.2, 0.6))
        rw_mutex.release()
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    # Create reader and writer threads
    readers = [threading.Thread(target=reader, args=(i, 3)) for i in range(2)]
    writers = [threading.Thread(target=writer, args=(i, 3)) for i in range(2)]

    # Start threads
    for t in readers + writers:
        t.start()

    # Wait for all threads to finish
    for t in readers + writers:
        t.join()

    print("Reader-Writer simulation finished.")

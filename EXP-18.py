# producer_consumer.py

import threading
import time
import random

# Shared buffer and size
buffer = []
BUFFER_SIZE = 5

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # initially buffer has BUFFER_SIZE empty slots
full = threading.Semaphore(0)             # initially buffer has 0 full slots
mutex = threading.Lock()                  # mutual exclusion lock

# Producer function
def producer(id, items=5):
    for i in range(items):
        item = f"item-{id}-{i}"
        empty.acquire()      # wait if buffer is full
        with mutex:          # enter critical section
            buffer.append(item)
            print(f"Producer {id} produced {item} | buffer size: {len(buffer)}")
        full.release()       # signal that buffer has a new item
        time.sleep(random.uniform(0.1, 0.5))

# Consumer function
def consumer(id, items=5):
    for i in range(items):
        full.acquire()       # wait if buffer is empty
        with mutex:          # enter critical section
            item = buffer.pop(0)
            print(f"Consumer {id} consumed {item} | buffer size: {len(buffer)}")
        empty.release()      # signal that buffer has an empty slot
        time.sleep(random.uniform(0.1, 0.5))

# Main execution
if __name__ == "__main__":
    # Create threads
    producers = [threading.Thread(target=producer, args=(i, 10)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(i, 10)) for i in range(2)]

    # Start threads
    for p in producers: p.start()
    for c in consumers: c.start()

    # Join threads
    for p in producers: p.join()
    for c in consumers: c.join()

    print("Producer-Consumer simulation finished.")

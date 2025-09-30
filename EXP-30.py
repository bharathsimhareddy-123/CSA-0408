import threading
import time
import random

counter = 0
mutex = threading.Lock()

def increment(thread_id, times=5):
    global counter
    for _ in range(times):
        mutex.acquire()
        local = counter
        local += 1
        counter = local
        print(f"Thread {thread_id} incremented counter to {counter}")
        mutex.release()
        time.sleep(random.uniform(0.1,0.3))

threads = [threading.Thread(target=increment, args=(i,5)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()

print("Final Counter:", counter)

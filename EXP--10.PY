from multiprocessing import Process, Queue
def producer(q):
    q.put("Hello from BHARATH")
def consumer(q):
    msg = q.get()
    print("Consumer received:", msg)
if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

from multiprocessing import Process, Value
def child(shared_val):
    shared_val.value = 100  
def parent():
    shared_val = Value('i', 0)  # shared integer
    p = Process(target=child, args=(shared_val,))
    p.start()
    p.join()
    print("Parent read from shared memory:", shared_val.value)
if __name__ == "__main__":
    parent()

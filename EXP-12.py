# dining_philosophers.py
import threading
import time

N = 5  # number of philosophers
forks = [threading.Lock() for _ in range(N)]

def philosopher(id, rounds=3):
    left = id
    right = (id + 1) % N
    for r in range(rounds):
        print(f"Philosopher {id} is thinking (round {r+1}).")
        time.sleep(0.5)

        # Order of picking forks to avoid deadlock
        if id % 2 == 0:
            first, second = right, left
        else:
            first, second = left, right

        with forks[first]:
            print(f"Philosopher {id} picked up fork {first}.")
            time.sleep(0.1)
            with forks[second]:
                print(f"Philosopher {id} picked up fork {second} and is eating.")
                time.sleep(0.5)

        print(f"Philosopher {id} finished eating (round {r+1}).")

if __name__ == "__main__":
    threads = []
    for i in range(N):
        t = threading.Thread(target=philosopher, args=(i,2))  # 2 rounds each
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Simulation finished.")

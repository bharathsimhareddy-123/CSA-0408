# disk_fcfs.py
# FCFS disk scheduling simulation: compute total head movement

def fcfs(requests, head):
    order = [head] + requests
    total_movement = sum(abs(order[i] - order[i-1]) for i in range(1, len(order)))
    return total_movement, requests

if __name__ == "__main__":
    req = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    movement, order = fcfs(req, head)
    print("Order served (FCFS):", order)
    print("Total head movement:", movement)

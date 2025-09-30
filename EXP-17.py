# bankers_algorithm.py

def is_safe(available, allocation, need):
    n = len(allocation)  # number of processes
    m = len(available)   # number of resources
    work = available[:]
    finish = [False]*n
    safe_seq = []

    while True:
        progressed = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_seq.append(i)
                progressed = True
        if not progressed:
            break

    return all(finish), safe_seq

def request_resources(available, allocation, maxm, proc_id, req):
    need = [[maxm[i][j] - allocation[i][j] for j in range(len(available))] for i in range(len(allocation))]

    if any(req[j] > need[proc_id][j] for j in range(len(available))):
        return False, "Error: Request exceeds maximum need."
    if any(req[j] > available[j] for j in range(len(available))):
        return False, "Resources not available."

    # Simulate allocation
    avail2 = available[:]
    alloc2 = [row[:] for row in allocation]
    for j in range(len(available)):
        avail2[j] -= req[j]
        alloc2[proc_id][j] += req[j]

    need2 = [[maxm[i][j] - alloc2[i][j] for j in range(len(available))] for i in range(len(allocation))]
    safe, seq = is_safe(avail2, alloc2, need2)
    if safe:
        return True, seq
    else:
        return False, "Request would lead to unsafe state."

if __name__ == "__main__":
    Available = [3, 3, 2]
    Max = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    Allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # Example request: Process 1 requests [1,0,2]
    proc_id = 1
    req = [1, 0, 2]
    granted, result = request_resources(Available, Allocation, Max, proc_id, req)
    print(f"Request by P{proc_id} for {req}:", "Granted" if granted else "Denied")
    print("Result:", result)

    # Check initial system safety
    need = [[Max[i][j]-Allocation[i][j] for j in range(len(Available))] for i in range(len(Allocation))]
    safe, seq = is_safe(Available, Allocation, need)
    print("\nIs the initial system safe?", safe)
    if safe:
        print("Safe sequence:", seq)

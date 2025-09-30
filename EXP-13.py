# memory_allocation.py

def first_fit(blocks, processes):
    alloc = [-1] * len(processes)
    b = blocks[:]
    for i, p in enumerate(processes):
        for j in range(len(b)):
            if b[j] >= p:
                alloc[i] = j
                b[j] -= p
                break
    return alloc, b

def best_fit(blocks, processes):
    alloc = [-1] * len(processes)
    b = blocks[:]
    for i, p in enumerate(processes):
        best = -1
        for j in range(len(b)):
            if b[j] >= p:
                if best == -1 or b[j] < b[best]:
                    best = j
        if best != -1:
            alloc[i] = best
            b[best] -= p
    return alloc, b

def worst_fit(blocks, processes):
    alloc = [-1] * len(processes)
    b = blocks[:]
    for i, p in enumerate(processes):
        worst = -1
        for j in range(len(b)):
            if b[j] >= p:
                if worst == -1 or b[j] > b[worst]:
                    worst = j
        if worst != -1:
            alloc[i] = worst
            b[worst] -= p
    return alloc, b

if __name__ == "__main__":
    blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    print("Blocks:", blocks)
    print("Processes:", processes)

    alloc, rem = first_fit(blocks, processes)
    print("\nFirst Fit Allocation:", alloc)
    print("Remaining Blocks:", rem)

    alloc, rem = best_fit(blocks, processes)
    print("\nBest Fit Allocation:", alloc)
    print("Remaining Blocks:", rem)

    alloc, rem = worst_fit(blocks, processes)
    print("\nWorst Fit Allocation:", alloc)
    print("Remaining Blocks:", rem)

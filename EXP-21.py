blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

allocation = [-1]*len(processes)

for i, p in enumerate(processes):
    worst_idx = -1
    for j, b in enumerate(blocks):
        if b >= p and (worst_idx == -1 or b > blocks[worst_idx]):
            worst_idx = j
    if worst_idx != -1:
        allocation[i] = worst_idx
        blocks[worst_idx] -= p

print("Process Allocation (Worst Fit):", allocation)
print("Remaining Blocks:", blocks)

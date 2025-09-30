blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

allocation = [-1]*len(processes)

for i, p in enumerate(processes):
    best_idx = -1
    for j, b in enumerate(blocks):
        if b >= p and (best_idx == -1 or b < blocks[best_idx]):
            best_idx = j
    if best_idx != -1:
        allocation[i] = best_idx
        blocks[best_idx] -= p

print("Process Allocation (Best Fit):", allocation)
print("Remaining Blocks:", blocks)

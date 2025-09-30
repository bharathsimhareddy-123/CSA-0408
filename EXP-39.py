# disk_cscan.py
# C-SCAN: scan in one direction and jump to other end without servicing during jump

def cscan(requests, head, disk_size):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    order = []
    total = 0
    cur = head

    # service right side up to end
    for r in right:
        order.append(r); total += abs(cur - r); cur = r
    # jump to start (no servicing during jump)
    total += abs(cur - (disk_size - 1))
    total += (disk_size - 1)  # from end to 0 as jump (conceptual distance)
    cur = 0
    for r in left:
        order.append(r); total += abs(cur - r); cur = r

    return total, order

if __name__ == "__main__":
    req = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53
    disk_size = 200
    total, seq = cscan(req, head, disk_size)
    print("Sequence (C-SCAN):", seq)
    print("Total head movement:", total)

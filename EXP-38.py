# disk_scan.py
# SCAN: head moves in one direction servicing requests, then reverses

def scan(requests, head, disk_size, direction='up'):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    order = []
    total = 0
    cur = head

    if direction == 'up':
        for r in right:
            order.append(r); total += abs(cur - r); cur = r
        # go to end
        total += abs(cur - (disk_size - 1)); cur = disk_size - 1
        for r in reversed(left):
            order.append(r); total += abs(cur - r); cur = r
    else:  # direction down
        for r in reversed(left):
            order.append(r); total += abs(cur - r); cur = r
        total += abs(cur - 0); cur = 0
        for r in right:
            order.append(r); total += abs(cur - r); cur = r

    return total, order

if __name__ == "__main__":
    req = [82, 170, 43, 140, 24, 16, 190]
    head = 50
    disk_size = 200
    total, seq = scan(req, head, disk_size, direction='up')
    print("Sequence (SCAN):", seq)
    print("Total head movement:", total)

# contiguous_allocation.py
# Simulate contiguous file allocation: files occupy contiguous blocks

class Disk:
    def __init__(self, total_blocks):
        self.total = total_blocks
        self.map = [None] * total_blocks  # None = free, otherwise filename

    def allocate_contiguous(self, filename, length):
        # find a run of 'length' free blocks
        run = 0
        start = 0
        for i in range(self.total):
            if self.map[i] is None:
                if run == 0:
                    start = i
                run += 1
                if run == length:
                    for j in range(start, start + length):
                        self.map[j] = filename
                    return start  # starting block
            else:
                run = 0
        return -1  # no space

    def deallocate(self, filename):
        for i in range(self.total):
            if self.map[i] == filename:
                self.map[i] = None

    def show(self):
        print(self.map)


if __name__ == "__main__":
    d = Disk(20)
    print("Allocating files contiguously:")
    print("fileA (5) at", d.allocate_contiguous("fileA", 5))
    print("fileB (3) at", d.allocate_contiguous("fileB", 3))
    d.show()
    d.deallocate("fileA")
    print("After deleting fileA:")
    d.show()
    print("Try allocating fileC (6):", d.allocate_contiguous("fileC", 6))
    d.show()

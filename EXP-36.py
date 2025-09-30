# linked_allocation.py
# Simulate linked allocation using block pointers

class DiskLinked:
    def __init__(self, total_blocks):
        self.total = total_blocks
        self.next_block = [-1] * total_blocks  # -1 = free, -2 = end, >=0 points to next block
        self.owner = [None] * total_blocks

    def allocate(self, filename, length):
        free_blocks = [i for i, owner in enumerate(self.owner) if owner is None]
        if len(free_blocks) < length:
            return False
        chosen = free_blocks[:length]
        for i in range(length):
            self.owner[chosen[i]] = filename
            if i < length - 1:
                self.next_block[chosen[i]] = chosen[i+1]
            else:
                self.next_block[chosen[i]] = -2  # end marker
        # return head and tail
        return chosen[0], chosen[-1]

    def deallocate(self, filename):
        for i in range(self.total):
            if self.owner[i] == filename:
                self.owner[i] = None
                self.next_block[i] = -1

    def show(self):
        print("Blocks:")
        for i in range(self.total):
            print(f"{i}: owner={self.owner[i]} next={self.next_block[i]}")

if __name__ == "__main__":
    d = DiskLinked(12)
    print("Alloc allocations:")
    print("fileX (4)->", d.allocate("fileX", 4))
    print("fileY (3)->", d.allocate("fileY", 3))
    d.show()
    d.deallocate("fileX")
    print("After deleting fileX:")
    d.show()

# indexed_allocation.py
# Simulate indexed allocation where each file has an index block listing block numbers

class DiskIndexed:
    def __init__(self, total_blocks):
        self.total = total_blocks
        self.free = set(range(total_blocks))
        self.index_table = {}  # filename -> index_block (list of block numbers)

    def allocate(self, filename, length):
        if len(self.free) < length + 1:
            return False
        # reserve index block (one block)
        index_block = self.free.pop()
        data_blocks = []
        for _ in range(length):
            data_blocks.append(self.free.pop())
        self.index_table[filename] = {"index_block": index_block, "blocks": data_blocks}
        return True

    def deallocate(self, filename):
        if filename in self.index_table:
            rec = self.index_table.pop(filename)
            self.free.add(rec["index_block"])
            for b in rec["blocks"]:
                self.free.add(b)

    def show(self):
        print("Index table:")
        for fn, rec in self.index_table.items():
            print(f"{fn}: index={rec['index_block']}, blocks={rec['blocks']}")
        print("Free blocks:", sorted(self.free))


if __name__ == "__main__":
    d = DiskIndexed(15)
    print("Allocating files with index blocks:")
    print("file1 (4) ->", d.allocate("file1", 4))
    print("file2 (3) ->", d.allocate("file2", 3))
    d.show()
    d.deallocate("file1")
    print("After deallocating file1:")
    d.show()

# random_access_employee.py
import struct
import os

# Define record format: id (int), name (20 bytes), salary (float)
RECORD_FMT = 'i20sf'
RECORD_SIZE = struct.calcsize(RECORD_FMT)
FILENAME = 'employees.dat'

# Pack employee data into binary format
def pack_record(emp_id, name, salary):
    name_bytes = name.encode('utf-8')[:20]
    name_bytes += b' ' * (20 - len(name_bytes))
    return struct.pack(RECORD_FMT, emp_id, name_bytes, float(salary))

# Unpack binary data to employee record
def unpack_record(data):
    emp_id, name_bytes, salary = struct.unpack(RECORD_FMT, data)
    return emp_id, name_bytes.decode('utf-8').rstrip(), salary

# Write a record at a specific record number
def write_record(rec_no, emp_id, name, salary):
    with open(FILENAME, 'r+b') as f:
        f.seek(rec_no * RECORD_SIZE)
        f.write(pack_record(emp_id, name, salary))

# Read a record at a specific record number
def read_record(rec_no):
    with open(FILENAME, 'rb') as f:
        f.seek(rec_no * RECORD_SIZE)
        data = f.read(RECORD_SIZE)
        if not data or len(data) < RECORD_SIZE:
            return None
        return unpack_record(data)

if __name__ == "__main__":
    # Create file with 5 empty records if not exists
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'wb') as f:
            for _ in range(5):
                f.write(pack_record(0, "", 0.0))

    # Write record #2
    write_record(2, 101, "Alice", 45000.0)

    # Read record #2
    rec = read_record(2)
    print("Record 2:", rec)

    # List all records
    print("\nAll Employee Records:")
    with open(FILENAME, 'rb') as f:
        i = 0
        while True:
            data = f.read(RECORD_SIZE)
            if not data:
                break
            print(f"Record {i}:", unpack_record(data))
            i += 1

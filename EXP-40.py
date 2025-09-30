# linux_permissions.py
# Illustrate Linux file permissions and user types

PERM_MAP = {'r':4, 'w':2, 'x':1, '-':0}

def octal_to_permission(octal):
    # octal is string like '754' or int 754
    s = str(octal)
    if len(s) != 3:
        raise ValueError("Expect 3-digit octal (owner-group-others)")
    perms = []
    for ch in s:
        v = int(ch)
        bits = ''.join(['r' if v & 4 else '-',
                        'w' if v & 2 else '-',
                        'x' if v & 1 else '-'])
        perms.append(bits)
    return ''.join(perms)  # e.g. 'rwxr-xr--'

def symbolic_to_octal(sym):
    if len(sym) != 9:
        raise ValueError("Expect 9-char symbolic (rwxrwxrwx)")
    vals = []
    for i in range(0, 9, 3):
        v = 0
        v += 4 if sym[i] == 'r' else 0
        v += 2 if sym[i+1] == 'w' else 0
        v += 1 if sym[i+2] == 'x' else 0
        vals.append(str(v))
    return int(''.join(vals))

def check_access(sym_perm, user_type, operation):
    # user_type in ['owner', 'group', 'others']
    idx = {'owner':0,'group':1,'others':2}[user_type]
    perm_chunk = sym_perm[idx*3: idx*3+3]
    op_map = {'read':'r','write':'w','execute':'x'}
    return op_map[operation] in perm_chunk

if __name__ == "__main__":
    print("Octal 754 -> symbolic:", octal_to_permission(754))
    print("Symbolic rwxr-xr-- -> octal:", symbolic_to_octal("rwxr-xr--"))
    sym = octal_to_permission(640)
    print("640 =>", sym)
    print("Can owner write? ", check_access(sym, 'owner', 'write'))
    print("Can group write? ", check_access(sym, 'group', 'write'))
    print("Can others read? ", check_access(sym, 'others', 'read'))

    # Illustrate user types (simulation)
    print("\nUser types in Linux (conceptual):")
    print("- root: superuser with effective UID 0, can bypass permission checks")
    print("- owner: the user who owns the file")
    print("- group: users who are members of the file's group")
    print("- others: everybody else")
    print("\nExamples:")
    print("File mode 644 (rw-r--r--): owner read/write, group read, others read")

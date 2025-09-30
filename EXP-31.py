# fifo_paging.py
# Simulate FIFO page replacement algorithm

def fifo_page_replacement(reference_string, frames_count):
    frames = []
    pointer = 0
    page_faults = 0
    steps = []

    for page in reference_string:
        hit = page in frames
        if not hit:
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frames_count
        steps.append((list(frames), page, hit, page_faults))
    return page_faults, steps

if __name__ == "__main__":
    ref = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    faults, s = fifo_page_replacement(ref, 3)
    print("Reference:", ref)
    for f, p, hit, pf in s:
        print(f"Access {p}: frames={f} {'HIT' if hit else 'MISS'} faults={pf}")
    print("Total page faults:", faults)

# lru_paging.py
# Simulate LRU page replacement algorithm

def lru_page_replacement(reference_string, frames_count):
    frames = []
    recent = []  # most recent at end
    page_faults = 0
    steps = []

    for page in reference_string:
        if page in frames:
            # update recent order
            recent.remove(page)
            recent.append(page)
            hit = True
        else:
            hit = False
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
                recent.append(page)
            else:
                # least recently used is at recent[0]
                lru = recent.pop(0)
                idx = frames.index(lru)
                frames[idx] = page
                recent.append(page)
        steps.append((list(frames), list(recent), page, hit, page_faults))
    return page_faults, steps

if __name__ == "__main__":
    ref = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    faults, s = lru_page_replacement(ref, 3)
    for frames, recent, p, hit, pf in s:
        print(f"Access {p}: frames={frames} recent={recent} {'HIT' if hit else 'MISS'} faults={pf}")
    print("Total page faults:", faults)

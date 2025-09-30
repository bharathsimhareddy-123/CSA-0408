# optimal_paging.py
# Simulate Optimal page replacement (needs future lookahead)

def optimal_page_replacement(reference_string, frames_count):
    frames = []
    page_faults = 0
    steps = []

    for i, page in enumerate(reference_string):
        if page in frames:
            hit = True
        else:
            hit = False
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                # choose page in frames with farthest next use (or never used again)
                farthest_index = -1
                to_replace = None
                for f in frames:
                    try:
                        idx = reference_string.index(f, i+1)
                    except ValueError:
                        idx = float('inf')  # not used again -> best candidate
                    if idx > farthest_index:
                        farthest_index = idx
                        to_replace = f
                frames[frames.index(to_replace)] = page
        steps.append((list(frames), page, hit, page_faults))
    return page_faults, steps

if __name__ == "__main__":
    ref = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    faults, s = optimal_page_replacement(ref, 3)
    for f, p, hit, pf in s:
        print(f"Access {p}: frame,mss={f} {'HIT' if hit else 'MISS'} faults={pf}")
    print("Total page faults:", faults)

def sjf_non_preemptive(processes, arrival_time, burst_time):
    n = len(processes)
    completed = [False] * n
    finish_time = [0] * n
    time = 0
    complete = 0
    while complete != n:
        idx = -1
        shortest_bt = float("inf")
        for i in range(n):
            if not completed[i] and arrival_time[i] <= time:
                if burst_time[i] < shortest_bt:
                    shortest_bt = burst_time[i]
                    idx = i
        if idx != -1:
            time += burst_time[idx]
            finish_time[idx] = time
            completed[idx] = True
            complete += 1
        else:
            time += 1  
    tat = [0] * n
    wt = [0] * n
    for i in range(n):
        tat[i] = finish_time[i] - arrival_time[i]
        wt[i] = tat[i] - burst_time[i]
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{finish_time[i]}\t{tat[i]}\t{wt[i]}")
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
processes = [1, 2, 3, 4]
arrival_time = [0, 2, 4, 5]
burst_time = [7, 4, 1, 4]
sjf_non_preemptive(processes, arrival_time, burst_time)

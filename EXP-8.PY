def round_robin(processes, burst_time, quantum):
    n = len(processes)
    remaining_bt = burst_time[:]
    time = 0
    completion_time = [0] * n
    queue = list(range(n))  
    while queue:
        i = queue.pop(0)
        if remaining_bt[i] > quantum:
            time += quantum
            remaining_bt[i] -= quantum
            queue.append(i)
        else:
            time += remaining_bt[i]
            remaining_bt[i] = 0
            completion_time[i] = time
    tat = [completion_time[i] for i in range(n)]
    wt = [tat[i] - burst_time[i] for i in range(n)]
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print("Process\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"P{processes[i]}\t{burst_time[i]}\t{completion_time[i]}\t{tat[i]}\t{wt[i]}")
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
processes = [1, 2, 3]
burst_time = [10, 5, 8]
quantum = 3
round_robin(processes, burst_time, quantum)

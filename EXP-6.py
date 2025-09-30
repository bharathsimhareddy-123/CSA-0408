def preemptive_priority_scheduling(processes, burst_time, arrival_time, priority):
    n = len(processes)
    remaining_bt = burst_time[:]
    complete = 0
    time = 0
    finish_time = [0] * n
    while complete != n:
        idx = -1
        highest_priority = -1
        for i in range(n):
            if arrival_time[i] <= time and remaining_bt[i] > 0:
                if priority[i] > highest_priority:
                    highest_priority = priority[i]
                    idx = i
        if idx != -1:
            remaining_bt[idx] -= 1
            time += 1
            if remaining_bt[idx] == 0:
                complete += 1
                finish_time[idx] = time
        else:
            time += 1 
    tat = [0] * n
    wt = [0] * n
    for i in range(n):
        tat[i] = finish_time[i] - arrival_time[i]
        wt[i] = tat[i] - burst_time[i]
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print("Process\tAT\tBT\tPriority\tCT\tTAT\tWT")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{priority[i]}\t\t{finish_time[i]}\t{tat[i]}\t{wt[i]}")
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
processes = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]
burst_time = [7, 4, 1, 4]
priority = [2, 3, 5, 4]  
preemptive_priority_scheduling(processes, burst_time, arrival_time, priority)

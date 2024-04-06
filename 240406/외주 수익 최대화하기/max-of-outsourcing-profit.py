def dfs(day: int, cost: int, job_list: list):
    if day == len(job_list):
        return cost
    
    period, earn = job_list[day]
    if day + period <= len(job_list):
        return max(dfs(day+period, cost+earn, job_list), dfs(day+1, cost, job_list))
    else :
        return dfs(day+1, cost, job_list)



n = int(input())
job_list = []
for day in range(n):
    job_list.append(list(map(int, input().split())))

print(dfs(0,0,job_list))
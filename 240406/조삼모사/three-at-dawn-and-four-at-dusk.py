n = int(input())

def get_work_balance(morning_works: list, works: list):
    morning_work_time = 0
    evening_work_time = 0
    
    for row in range(len(works)):
        for col in range(len(works[0])):
            if row == col :
                continue
            work_time = works[row][col]
            if mornig_works[row] and mornig_works[col]:
                morning_work_time += work_time
            elif not mornig_works[row] and not mornig_works[col]:
                evening_work_time += work_time

    return abs(morning_work_time-evening_work_time)


def dfs(day: int, morning_works: list, works: list):
    if day == len(works):
        return get_work_balance(morning_works, works)
    

    # work morning_works
    morning_works[day] = True
    answer = dfs(day+1, morning_works, works)

    # work evening
    morning_works[day] = False
    answer = min(answer, dfs(day+1, morning_works, works))
    return answer
    


works = []
for row in range(n):
    works.append(list(map(int, input().split())))


mornig_works = [False] * n 
print(dfs(0, mornig_works, works))
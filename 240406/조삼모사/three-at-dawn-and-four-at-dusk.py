n = int(input())

# This function calculates the difference in work time between morning and evening.
def get_work_balance(morning_works: list, works: list):
    morning_work_time = 0
    evening_work_time = 0
    
    for row in range(len(works)):
        for col in range(len(works[0])):
            if row == col:
                continue
            work_time = works[row][col]
            # Corrected variable name from 'mornig_works' to 'morning_works'
            if morning_works[row] and morning_works[col]:
                morning_work_time += work_time
            elif not morning_works[row] and not morning_works[col]:
                evening_work_time += work_time
    return abs(morning_work_time - evening_work_time)

# This function uses depth-first search to explore all combinations of morning and evening work.
def dfs(day: int, morning_works: list, works: list):
    if day == len(works):
        return get_work_balance(morning_works, works)
    
    # Option for working in the morning.
    morning_works[day] = True
    morning_option = dfs(day+1, morning_works, works)

    # Option for working in the evening.
    morning_works[day] = False
    evening_option = dfs(day+1, morning_works, works)

    # Returning the minimum difference to ensure the best balance.
    return min(morning_option, evening_option)

# Reading the matrix of work times.
works = []
for row in range(n):
    works.append(list(map(int, input().split())))

morning_works = [False] * n 
print(dfs(0, morning_works, works))
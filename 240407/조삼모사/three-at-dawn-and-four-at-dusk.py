def get_work_balance(morning_works: list, works: list):
    morning_work_time = 0
    evening_work_time = 0


    
    for row in range(len(works)):
        for col in range(len(works[0])):
            if row == col :
                continue
            work_time = works[row][col]
            if morning_works[row] and morning_works[col]: 
                morning_work_time += work_time
            elif not morning_works[row] and not morning_works[col]:
                evening_work_time += work_time

    return abs(morning_work_time-evening_work_time)


def dfs(day: int, morning_works: list, works: list):
    # 균등하게 일을 나눴을때 
    if morning_works.count(True) == morning_works.count(False):
        return get_work_balance(morning_works, works)

    elif day == len(works) :
        return float("inf")


    # work morning_works
    morning_works[day] = True
    answer = dfs(day+1, morning_works, works)

    # work evening
    morning_works[day] = False
    answer = min(answer, dfs(day+1, morning_works, works))
    return answer
    
# 입력
n = int(input())
works = []
for row in range(n):
    works.append(list(map(int, input().split())))

# works 에 넣어요

# 아침에 무슨 일을 할건지
mornig_flag = [False] * n 
print(dfs(0, mornig_flag, works))
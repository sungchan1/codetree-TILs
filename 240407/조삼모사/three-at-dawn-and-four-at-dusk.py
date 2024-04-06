import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
p = [
    list(map(int, input().split()))
    for _ in range(n)
]
evening = [
    False for _ in range(n)
]

ans = INT_MAX


# 아침과 저녁 간의 힘듦의 차이를 계산합니다.
def calc():
    morning_sum = sum([
        p[i][j]  
        for i in range(n)
        for j in range(n)
        if not evening[i] and not evening[j]
    ])
    evening_sum = sum([
        p[i][j]  
        for i in range(n)
        for j in range(n)
        if evening[i] and evening[j]
    ])
        
    return abs(morning_sum - evening_sum)


def find_min(curr_idx, cnt):
    global ans
    
    # 정확히 아침 / 저녁으로 n / 2개씩 일이 나뉜 경우에만
    if cnt == n // 2:
        # 선택된 조합에 대해 합의 차이를 계산하여
        # 그 중 최솟값을 찾습니다.
        ans = min(ans, calc())
        return
    
    # n개에 대해 전부 결정했음에도
    # n / 2 개로 나뉘지 못한 경우라면
    # 바로 퇴각합니다.
    if curr_idx == n:
        return

    # curr_idx 번째 업무를 아침에 하는 경우
    find_min(curr_idx + 1, cnt)
    
    # curr_idx 번째 업무를 저녁에 하는 경우
    evening[curr_idx] = True
    find_min(curr_idx + 1, cnt + 1)
    evening[curr_idx] = False


find_min(0, 0)

# 출력:
print(ans)
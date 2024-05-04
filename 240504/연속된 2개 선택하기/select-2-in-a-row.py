def max_sum_with_constraints(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]  # 두 개만 있을 경우, 두 개 모두 더하는 것이 최대값
    
    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = arr[0]
    dp[2] = arr[0] + arr[1]
    dp[3] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    
    for i in range(4, n + 1):
        dp[i] = max(dp[i-1], arr[i-1] + dp[i-2], arr[i-1] + arr[i-2] + dp[i-3])
    
    return dp[n]

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 결과 출력
print(max_sum_with_constraints(arr))
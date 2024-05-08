def max_grouped_score(n, numbers):
    if n == 0:
        return 0
    
    # 수열 정렬
    numbers.sort()

    # 점수를 계산할 변수
    max_score = 0

    # 음수 처리 - 음수는 작은 것부터 묶어야 큰 양수가 됨
    i = 0
    while i < n and numbers[i] < 0:
        if i + 1 < n and numbers[i + 1] < 0:
            # 연속된 음수 두 개를 곱해서 점수 추가
            max_score += numbers[i] * numbers[i + 1]
            i += 2
        else:
            # 홀수 개의 음수가 남았을 때 마지막 하나 처리
            max_score += numbers[i]
            i += 1
    
    # 양수 처리 - 양수는 큰 것부터 묶어야 더 큰 수가 됨
    j = n - 1
    while j >= 0 and numbers[j] > 1:
        if j - 1 >= 0 and numbers[j - 1] > 1:
            # 큰 양수 두 개를 곱해서 점수 추가
            max_score += numbers[j] * numbers[j - 1]
            j -= 2
        else:
            # 1 또는 그보다 작은 양수는 단독으로 처리하는 것이 낫다
            max_score += numbers[j]
            j -= 1
    
    # 1이나 0의 처리 (1이면 더하는 것과 곱하는 것이 같으므로 단독으로 더하고, 0이면 무시)
    while i <= j:
        max_score += numbers[j]
        j -= 1

    return max_score

# 테스트 케이스
n = 4
numbers = [-2, 1, 1, 3]
print(max_grouped_score(n, numbers))  # 출력: 3 (예제에서 기대하는 결과)
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()


total_sum = sum(numbers)
target_diff = total_sum - S

left, right = 0, len(numbers) - 1
min_diff = float('inf')
best_pair = None

while left < right:
    pair_sum = numbers[left] + numbers[right]
    diff = abs(target_diff - pair_sum)

    if diff < min_diff:
        min_diff = diff
        best_pair = (numbers[left], numbers[right])
    
    # 조건에 따라 포인터 이동
    if pair_sum < target_diff:
        left += 1
    else:
        right -= 1

remaining_sum = total_sum - sum(best_pair)
result = abs(S - remaining_sum)
print(result)
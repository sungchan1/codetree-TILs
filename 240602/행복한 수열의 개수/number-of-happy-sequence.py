N, M = map(int, input().split())

numbers = []

for _ in range(N):
    numbers.append(list(map(int, input().split())))

# 가로

result = 0
for row in range(N):
    count = 1
    for i in range(N):
        target = numbers[row][i]
        if i == 0:
            last = target
            count = 1
            if count >= M:
                result += 1
                break
            continue
        
        if last == target:
            count +=1

        else :
            last = target
            count = 1

        if count >= M:
            result += 1
            break

# 세로
for col in range(N):
    count = 1
    for i in range(N):
        target = numbers[i][col]
        if i == 0:
            last = target
            count = 1
            if count >= M:
                result += 1
                break
            continue
        
        if last == target:
            count +=1

        else :
            last = target
            count = 1

        if count >= M:
            result += 1
            break

print(result)
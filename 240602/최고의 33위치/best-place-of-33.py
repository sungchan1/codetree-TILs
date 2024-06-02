maps = []



N = int(input())



for row in range(N):
    maps.append(list(map(int, input().split())))

result = -float('inf')


for row in range(1, N-1):
    for col in range(1, N-1):
        score = sum(maps[row-1][col-1:col+2]) + \
                sum(maps[row][col-1:col+2]) + \
                sum(maps[row+1][col-1:col+2])
        result = max(score, result)
print(result)
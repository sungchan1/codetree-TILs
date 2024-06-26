from sys import stdin as s

# s = open("input.txt", "r")



N, M = map(int, s.readline().split())
numbers = [
    list(map(int, s.readline().split()))
    for _ in range(N)
]

result = -float('inf')

for row in range(N):
    for col in range(M):
        # line
        # vertical
        if row+2 < N:
            result = max(result, sum([numbers[row][col], numbers[row+1][col], numbers[row+2][col]]))
        # horizontal
        if col+2 < M:
            result = max(result, sum(numbers[row][col:col+3]))
            # print(f"{row}, {col}, {sum(numbers[row][col:col+3])}")
            
    # tromino
        if row+1 < N and col+1 < M:
            result = max(result, sum([numbers[row][col], numbers[row+1][col], numbers[row][col+1]]))
            result = max(result, sum([numbers[row][col], numbers[row+1][col], numbers[row+1][col+1]]))
            result = max(result, sum([numbers[row][col], numbers[row][col+1], numbers[row+1][col+1]]))
            result = max(result, sum([numbers[row+1][col], numbers[row][col+1], numbers[row+1][col+1]]))

print(result)
n = int(input())

houses = list(map(int, input().split()))


walks = [0] * n
for i in range(n):
    for j in range(n):
        walks[j] += abs(i-j) * houses[i]

print(min(walks))
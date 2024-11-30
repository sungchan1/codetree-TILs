N, H, T = map(int, input().split())

field = list(map(int, input().split()))

costs = [

    abs(H-height)
    for height
    in field
]

result = float("inf")


for i in range(N-T):
    target = sum(costs[i:i+T])
    result = min(result, target)


print(result)

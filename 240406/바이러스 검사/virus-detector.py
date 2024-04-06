from sys import stdin as s
import math
n = int(s.readline())
result = 0
customers = list(map(int, s.readline().split()))
leader, teamone = map(int, s.readline().split())

for customer in customers:
    result += 1
    customer -= leader
    if customer > 0:
        result += math.ceil(customer/teamone)

print(result)
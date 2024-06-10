N = int(input())
cows = list(map(int, input().split()))


result = 0
for i in range(N):
    for j in range(i+1, N):
        if cows[i] > cows[j]:
            continue

        for k in range(j+1, N):
            if cows[j] > cows[k]:
                continue
            else:
                result +=1 

print(result)
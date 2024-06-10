N = int(input())
coins = [
    list(map(int, input().split()))
    for i in range(N)
]



def get_coins(row, col):
    coin = 0
    for i in range(col-1, col+2):
        if coins[row][i] == 1:
            coin += 1

    return coin
                
result = 0
for row in range(N):
    for col in range(1,N-1):
        result = max(result, get_coins(row, col))
        
    
print(result)
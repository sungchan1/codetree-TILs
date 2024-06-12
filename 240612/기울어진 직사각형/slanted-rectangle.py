# 입력을 받고
n = int(input())
numbers = [
    list(map(int, input().split()))
]


def get_score(row, col, vertical, horizontal):
    
    point = [row,col]

    dx = [1,-1,-1,1]
    dy = [-1,-1,1,1]
    
    for i range(4):
        if i % 2 == 0:
            point[0] = point[0] + dy[i]*vertical
            point[1] = point[1] + dx[i]*vertical
        else:
            point[0] = point[0] + dy[i]*horizontal
            point[1] = point[1] + dx[i]*horizontal

        

        


    return score


# row, col로 시작 부분을 정하고
for row in range(n):
    for col in range(n):
        start = row,col
        for vertical in range(1,n):
            for horizontal in range(1,n):
                get 

# 1번가고
# 2번가고
# 3번 가고
# 4번 가고
# 제 자리면 result에 넣음
# 단 밖으로 나가면 나가리
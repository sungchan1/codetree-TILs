# import sys
# sys.stdin = open("input.txt","r")

MAX_L = 70

R, C, K = 0, 0, 0
planet = [[0] * MAX_L for _ in range(MAX_L + 3)]
visited = []

# 0 : nothing, 1: normal 2: root 3: exit
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dp = {}
answer = 0 #


FAIL_DROP = 0

def check_movable(r,c, nr,nc):
    global planet, visited, R, C

    if nr < 0 or nr > R+2 or nc <0 or nc > C-1:
        return False

    if visited[nr][nc]:
        return False

    cell_type= planet[r][c]
    next_cell_type = planet[nr][nc]

    if next_cell_type == 0:
        return False

    if cell_type == 1:
        if next_cell_type == 2:
            return True

    elif cell_type == 2:
        if next_cell_type == 1 or next_cell_type == 3:
            return True

    elif cell_type == 3:
        if next_cell_type == 1 or next_cell_type == 3 or next_cell_type == 2:
            return True
    else:
        raise ValueError("FAIL : cell_type")
    return False


def move_robot(score:int, row: int, col: int):
    global R, visited, dp

    visited[row][col] = True
    if row == R+2:
        dp[(row,col)] = row
        return row
    elif (row,col) in dp.keys():
        return dp[(row,col)]

    score = max(score, row)

    # 상
    if check_movable(row,col, row-1, col):
        score = max(score, move_robot(score, row-1, col))
    # 하
    if check_movable(row,col, row+1, col):
        score = max(score, move_robot(score, row+1, col))
    # 좌
    if check_movable(row,col, row, col-1):
        score = max(score, move_robot(score, row, col-1))
    # 우
    if check_movable(row,col, row, col+1):
        score = max(score, move_robot(score, row, col+1))

    if score == R+2:
        dp[(row,col)] = score

    return score
def reset_planet():
    global planet, dp
    dp = {}
    for i in range(R + 3):
        for j in range(C):
            planet[i][j] = 0

def drop_rocket(column, direction) -> int:
    global R,C, planet, dx, dy

    row = 1 # 1 -3 베이스
    col = column


    def check_down(r,c) -> bool :
        if planet[r+2][c] == 0 and planet[r+1][c+1] == 0 and planet[r+1][c-1] == 0:
            return True
        return False

    def check_left(r, c) -> bool :
        if c <= 1:
            return False
        if planet[r][c-2] == 0 and planet[r-1][c-1] == 0 and planet[r+1][c-1] == 0:
            return True
        return False

    def check_right(r, c) -> bool :
        if c >= C-2:
            return False
        if planet[r][c+2] == 0 and planet[r-1][c+1] == 0 and planet[r+1][c+1] == 0:
            return True
        return False

    def check_planet_over():
        if row <= 3:
            # print(f"FAIL DROP")
            return True
        return False

    while True:
        if row == R+1:
            break
        elif check_down(row,col):
            row = row+1
            continue
        elif check_left(row, col) and check_down(row, col-1):
            row = row + 1
            col = col -1
            direction = (direction - 1) % 4
            continue
        elif check_right(row,col) and check_down(row,col+1) :
            row = row+1
            col = col + 1
            direction = (direction + 1) % 4
            continue
        else:
            break



    if check_planet_over():
        reset_planet()
        return FAIL_DROP
    # print(f"drop ({col},{row-3} {direction})")

    planet[row][col] = 2
    planet[row-1][col] = 1
    planet[row+1][col] = 1
    planet[row][col-1] = 1
    planet[row][col+1] = 1

    exit_row = row + dx[direction]
    exit_col = col + dy[direction]
    planet[exit_row][exit_col] = 3

    score = move_robot(0,row,col) -2
    return score





def main():
    global R, C, K, visited, dp
    R, C, K = map(int, input().split())
    answer= 0
    for id in range(1, K + 1): # 골렘 번호 id
        visited = [[False] * MAX_L for _ in range(MAX_L+3)]
        x, d = map(int, input().split()) # 골렘의 출발 x좌표, 방향 d를 입력받습니다
        x = x-1
        score = drop_rocket(x,d)
        answer += score
        # print(f"{answer}, {score}")
    print(answer)

if __name__ == "__main__":
    main()
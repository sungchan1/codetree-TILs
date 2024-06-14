def count_paths(grid, R, C):
    def is_valid(x, y):
        return 0 <= x < R and 0 <= y < C

    def dfs(x, y, path, prev_color):
        if len(path) > 4:
            return
        
        if (x, y) == (R-1, C-1):
            if len(path) == 4:
                nonlocal count
                count += 1
            return
        
        for i in range(x+1, R):
            for j in range(y+1, C):
                if grid[i][j] != prev_color:
                    dfs(i, j, path + [(i, j)], grid[i][j])
    
    count = 0
    dfs(0, 0, [(0, 0)], grid[0][0])
    return count

# 입력 처리
R, C = map(int, input().split())
grid = [input().split() for _ in range(R)]

# 결과 출력
print(count_paths(grid, R, C))
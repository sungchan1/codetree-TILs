def check_range(diff, low, high):
    return low <= diff <= high

def get_splites(egg_plate, low, high):
    n = len(egg_plate)
    splites = []
    for row in range(n):
        for col in range(n):
            if col < n - 1:  # Check right
                diff = abs(egg_plate[row][col] - egg_plate[row][col+1])
                if check_range(diff, low, high):
                    splites.append([(row, col), (row, col+1)])
            if row < n - 1:  # Check down
                diff = abs(egg_plate[row][col] - egg_plate[row+1][col])
                if check_range(diff, low, high):
                    splites.append([(row, col), (row+1, col)])
    return splites            

def merge_splites(splites, n):
    parent = {}
    def find(p):
        if parent[p] != p:
            parent[p] = find(parent[p])
        return parent[p]

    def union(p, q):
        rootP = find(p)
        rootQ = find(q)
        if rootP != rootQ:
            parent[rootQ] = rootP

    # Initialize parent for each cell
    for row in range(n):
        for col in range(n):
            parent[(row, col)] = (row, col)

    # Apply union
    for p1, p2 in splites:
        union(p1, p2)

    # Group by parent
    groups = {}
    for key in parent:
        root = find(key)
        if root not in groups:
            groups[root] = []
        groups[root].append(key)

    return list(groups.values())

def simulate(egg_plate, L, R):
    n = len(egg_plate)
    count = 0
    while True:
        splites = get_splites(egg_plate, L, R)
        if not splites:
            break
        merged_splites = merge_splites(splites, n)
        for group in merged_splites:
            egg_sum = sum(egg_plate[r][c] for r, c in group)
            egg_average = egg_sum // len(group)
            for r, c in group:
                egg_plate[r][c] = egg_average
        count += 1
    return count

# Example Usage
n, L, R = map(int, input().split())
egg_plate = [list(map(int, input().split())) for _ in range(n)]
result = simulate(egg_plate, L, R)
print(result)
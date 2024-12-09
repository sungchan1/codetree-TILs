from collections import deque

n = int(input())

def bfs():
    queue = deque()
    queue.append(([], [False] * (n + 1)))  
    while queue:
        current_answer, visited = queue.popleft()

  
        if len(current_answer) == n:
            print(" ".join(map(str, current_answer)))
            continue

        for next_index in range(1, n + 1):
            if not visited[next_index]:
                new_answer = current_answer + [next_index]
                new_visited = visited[:]
                new_visited[next_index] = True
                queue.append((new_answer, new_visited))

bfs()
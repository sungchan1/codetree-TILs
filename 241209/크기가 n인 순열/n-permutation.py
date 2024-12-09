n = int(input())


answer = []
visited = [False] * (n+1)




def dfs(count):

    if count == n+1:
        print(" ".join(map(str, answer)))


    for next_index in range(1, n+1):
        if visited[next_index]:
            continue

        visited[next_index] = True
        answer.append(next_index)
        dfs(count+1)
        answer.pop()
        visited[next_index] = False
    

dfs(1)
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [[False] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    
    visited[x] = True

    for i in graph[x]:
        if visited[i] != True:
            dfs(i)

    return 1

res = 0

for i in range(1,len(graph)):
    if visited[i] != True:
        res += dfs(i)

print(res)

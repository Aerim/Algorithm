n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

res = []
# global변수로 cnt 더해도 됨
def dfs(graph,c,visited,cnt):

    visited[c] = True
    res.append(c)

    for i in graph[c]:

        if visited[i] == False:
            dfs(graph,i,visited,cnt+1)

dfs(graph,1,visited,0)
print(len(res) - 1)

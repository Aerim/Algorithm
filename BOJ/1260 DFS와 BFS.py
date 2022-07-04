from collections import deque

n, m, v = map(int,input().split())

# _graph = [[]]
_graph = [[] for _ in range(n + 1)]

for i in range(m):
    a,b = map(int,input().split())
    _graph[a].append(b)
    _graph[b].append(a)

# 작은순서부터 방문
for i in range(len(_graph)):
    _graph[i].sort()

visited_b = [0 for _ in range(n + 1)]
visited_d = [0 for _ in range(n + 1)]

def bfs(v,graph,visited_b):

    que = deque()
    que.append(v)
    visited_b[v] = 1

    while que:
        q = que.popleft()
        print(q, end=' ')
       
        for g in graph[q]:
            if visited_b[g] != 1:
                que.append(g)
                visited_b[g] = 1

def dfs(v,graph,visited_d):

    visited_d[v] = 1
    print(v, end = ' ')

    for i in graph[v]:
        if visited_d[i] == 0:
            dfs(i, graph, visited_d)

dfs(v,_graph,visited_d)
print('')
bfs(v,_graph,visited_b)



# 최단경로 - bfs
from collections import deque
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

# 2개의 자연수가 주어지니까 가능
for i in range(m):
    a,b = map(int,input().split())
    # 인접행렬으로 변경
    graph[a].append(b)

visited = [False] * (n+1)
weight = [0] * (n+1)
answer = []

def bfs(v,visited,weight):
    
    visited[v] = True
    que = deque([v])
    
    while que:    
        
        v = que.popleft()
        
        for i in graph[v]:
            if visited[i] != True:
                visited[i] = True
                que.append(i)
                weight[i] = weight[v] + 1
    
bfs(x,visited,weight)

for w in range(len(weight)):
    if weight[w] == k:
        print(w)
        answer.append(w)
        
if len(answer) == 0:
    print(-1)
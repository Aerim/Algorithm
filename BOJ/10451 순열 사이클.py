from collections import deque

t = int(input())
res = []

def bfs(x):

    que = deque()
    que.append(x)
    visited[x] = True
    
    while que:

        p = que.popleft()

        for i in graph[p]:

            if visited[i] != True:
                que.append(i)
                visited[i] = True

for i in range(t):

    n = int(input())

    temp = list(map(int,input().split()))

    visited = [[False] for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]

    for i in range(len(temp)):
        graph[i+1].append(temp[i])

    cnt = 0

    for i in range(1,len(graph)):
        
        if visited[i] != True:
            bfs(i)
            cnt += 1

    res.append(cnt)

for i in res:
    print(i)
 
 



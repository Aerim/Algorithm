from collections import deque

n = int(input())
arr = list(map(int,input().split()))
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)] 

del_node = int(input())

visited[del_node] = True

for i,j in enumerate(arr):
    
    if j == -1:
        x = i
        que = deque()
        que.append(x)
        visited[x] = True
    else:
        
        if i == del_node:
            if del_node in graph[j]:
                graph[j].remove(del_node)
        else:
            graph[j].append(i)

if del_node == x:
    print(0)

else:
    cnt = 0

    while que:

        p = que.popleft()

        for i in graph[p]:
                if visited[i] == False:
                    que.append(i)
                    visited[i] = True

    for i in range(n):
    
        if visited[i] == True and len(graph[i]) == 0 and i != del_node:
        
            cnt += 1

    print(cnt)




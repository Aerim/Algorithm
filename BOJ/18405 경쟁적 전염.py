from collections import deque

n, k = map(int,input().split())

graph = []
virus = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(map(int,input().split())))
    
    for j in range(n):
        if graph[i][j] > 0 :
            virus.append((graph[i][j],i,j,0))
            
s, x, y = map(int,input().split())

# 바이러스가 종류가 낮은 애들부터 증식하니까 정렬해줌
virus.sort()
que = deque(virus)
            
while que:
    
    v, _x, _y, time = que.popleft()
    
    if time == s:
        break
    
    for i in range(4):
        
        nx = _x + dx[i]
        ny = _y + dy[i]
        
        if nx < 0  or nx >= n or ny < 0 or ny >= n:
            continue
        
        if graph[nx][ny] == 0:
            graph[nx][ny] = v
            time += 1
            que.append((v,nx,ny,time))

print(graph[x-1][y-1])
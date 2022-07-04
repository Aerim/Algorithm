from collections import deque

m, n = map(int,input().split())
graph = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

que = deque()

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i,j))
    
def bfs():

    while que:

        _x, _y = que.popleft()

        for i in range(4):

            nx = _x + dx[i]
            ny = _y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                  
            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[_x][_y] + 1
                que.append((nx,ny))
  
bfs()
res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        res = max(res,graph[i][j])
    
print(res - 1)

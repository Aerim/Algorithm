from collections import deque

n, m = map(int,input().split())

graph = []
visited = []
que = deque()

for i in range(n):
  graph.append(list(map(int,input().split())))
  visited.append([False] * m)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      graph[i][j] = 0 
      que.append((i,j))
      visited[i][j] = True
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while que:

  x, y = que.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < m:
      if visited[nx][ny] != True and graph[nx][ny] == 1:
        graph[nx][ny] += graph[x][y]
        visited[nx][ny] = True
        que.append((nx,ny))

for i in range(n):
  for j in range(m):
    if visited[i][j] != True and graph[i][j] == 1:
      graph[i][j] = -1

for i in graph:
  print(*i)
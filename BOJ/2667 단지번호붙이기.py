from collections import deque

n = int(input())
arr = []
res = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = []

for i in range(n):
    arr.append(list(map(int,input())))
    visited.append([0 * n for _ in range(n)])

def bfs(x,y):

    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    _cnt = 1

    while que:

        x, y = que.popleft()
    
        for i in range(4):
        
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                _cnt += 1
                que.append((nx,ny))
                visited[nx][ny] = 1
    
    return _cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            res.append(bfs(i,j))

print(len(res))

res = sorted(res)

for i in res:
    print(i)
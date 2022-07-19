from collections import deque

m , n = map(int,input().split())

arr = []
visited = []

for i in range(m):
    arr.append(list(map(int,input().split())))
    visited.append([False] * n)

cnt = 0

def bfs(y,x):

    # 대각선도 포함
    dx = [1,-1,0,0,-1,1,1,-1]
    dy = [0,0,-1,1,-1,-1,1,1]

    que = deque()
    que.append((y,x))
    visited[y][x] = True

    while que:

        _y, _x = que.popleft()

        for i in range(8):

            nx = _x + dx[i]
            ny = _y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[ny][nx] != True:
                visited[ny][nx] = True
                if arr[ny][nx] == 1:
                    que.append((ny,nx))

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == False :
            bfs(i,j)
            cnt += 1

print(cnt)


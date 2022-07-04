from collections import deque

n, m = map(int,input().split())
arr = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

visited1 = []

for i in range(m):
    arr.append(list(input()))

visited1 = [[0] * n for i in range(m)]

enemy = 0
our = 0

def bfs(x,y,color):

    que = deque()
    que.append((x,y))
    visited1[x][y] = 1
    cnt = 0

    while que:

        x, y = que.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n :
                continue

            if arr[nx][ny] == color and visited1[nx][ny] == 0:
                cnt += 1
                que.append((nx,ny))
                visited1[nx][ny] = 1

    return cnt + 1

for i in range(m):
    for j in range(n):
        if arr[i][j] == 'W' and visited1[i][j] != 1:
            our += bfs(i,j,'W') ** 2
        elif arr[i][j] == 'B' and visited1[i][j] != 1:
            enemy += bfs(i,j,'B') ** 2

print(our, enemy)
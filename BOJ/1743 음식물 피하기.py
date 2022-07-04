from collections import deque

n, m, k = map(int,input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

arr = [[0] * m for _ in range(n)]

for i in range(k):
    a, b = map(int,input().split())
    arr[a-1][b-1] = 1

def bfs(arr,x,y):

    que = deque()
    que.append((x,y))
    arr[x][y] = 2
    cnt = 0

    while que:

        _x, _y = que.popleft()

        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == 1:
                que.append((nx,ny))
                arr[nx][ny] = 2
                cnt += 1

    return cnt + 1

res = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            res.append(bfs(arr,i,j))

print(max(res))
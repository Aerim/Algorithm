from collections import deque

n, m = map(int, input().split())

arr = []
visited = []
x,y = 0, 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    arr.append(list(map(int,input())))

for i in range(n):
    visited.append([0 for _ in range(m)])

que = deque()
que.append((x,y))
visited[x][y] = 1

while que:

    _x, _y= que.popleft()

    for i in range(4):

        nx = _x + dx[i]
        ny = _y + dy[i]

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if arr[nx][ny] == 1 and visited[nx][ny] == 0:

            arr[nx][ny] += arr[_x][_y]
            que.append((nx, ny))

print(arr[n-1][m-1])
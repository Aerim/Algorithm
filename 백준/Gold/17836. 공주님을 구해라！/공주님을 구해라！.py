from collections import deque

n, m, t = map(int,input().split())

arr = []
visited = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    visited.append(list(False for _ in range(m)))

x, y = 0, 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

que = deque()
que.append((x,y))
visited[x][y] = True

dist = 0

# 칼 있을 때 거리랑 그냥 구했을 때 비교해서 최솟값
while que:

    _x, _y = que.popleft()
    
    for i in range(4):

        nx = _x + dx[i]
        ny = _y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        elif arr[nx][ny] == 0 and visited[nx][ny] == False:
            que.append((nx,ny))
            visited[nx][ny] = True
            arr[nx][ny] = arr[_x][_y] + 1
        
        elif arr[nx][ny] == 2 and visited[nx][ny] == False:
            visited[nx][ny] = True
            dist = arr[_x][_y] + 1 + (n-1 - nx) + (m-1 - ny)

# 그람을 먼저 뽑아야 하는 경우 계산 -> 11
# 5 4 100
# 0 1 2 1
# 0 1 0 1
# 0 0 0 0
# 1 1 1 1
# 0 0 0 0

if arr[n-1][m-1] > 0 and dist > 0:
    res = min(arr[n-1][m-1], dist)

elif arr[n-1][m-1] > 0 and dist == 0:
    res = arr[n-1][m-1]
elif arr[n-1][m-1] == 0 and dist > 0:
    res = dist
else:
    res = 0

if 0 < res <= t:
    print(res)
else:
    print('Fail')
from collections import deque

n = int(input())
arr = []
res = []
max_v = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)

    if max_v < max(temp):
        max_v = max(temp)
        
def bfs(x,y,h,visited):

    que = deque()
    que.append((x,y))
    
    visited[x][y] = True

    while que: 

        _x, _y = que.popleft()

        for i in range(4):

            nx = _x + dx[i]
            ny = _y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
        
            if arr[nx][ny] >=h and visited[nx][ny] == False:
                visited[nx][ny] = True
                que.append((nx,ny))
    
    return True

for h in range(1,max_v+1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= h and visited[i][j] == False:
                
                if bfs(i,j,h,visited) == True:
                    cnt += 1

    res.append(cnt)

print(max(res))

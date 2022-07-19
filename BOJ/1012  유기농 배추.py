from collections import deque

t = int(input())

for i in range(t):
    m, n, k = map(int,input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    cnt = 0

    for i in range(k):

        y, x = map(int,input().split())
        arr[x][y] = 1
        
    def bfs(x,y):
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        que = deque()
        que.append((x,y))
       
        while que:

            _x, _y = que.popleft()

            for i in range(4):
        
                nx = _x + dx[i]
                ny = _y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    que.append((nx,ny))
    

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1

        
    print(cnt)




 
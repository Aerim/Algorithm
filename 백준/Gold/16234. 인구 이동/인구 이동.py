from collections import deque

n, l, r = map(int,input().split())
arr = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    arr.append(list(map(int,input().split())))

def bfs(i,j,_visited):
    
    que = deque()
    que.append((i,j))
    unit = []
    unit.append((i,j))
    p_sum = arr[i][j]
    _visited[i][j] = True
    
    while que:
        
        x, y = que.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            
            if l <= abs(arr[x][y] - arr[nx][ny]) <= r and not _visited[nx][ny]:
                _visited[nx][ny] = True
                unit.append((nx,ny))
                que.append((nx,ny))
                p_sum += arr[nx][ny]
                
    temp = p_sum // len(unit)
    
    for k,v in unit:
        arr[k][v] = temp
        
    return len(unit)
   
cnt = 0  
        
while True:
    visited = [[False] * n for _ in range(n)]

    flag = False 

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                if bfs(i,j,visited) > 1:
                    flag = True
    
    if not flag:
        print(cnt)
        break

    cnt += 1  
    
     
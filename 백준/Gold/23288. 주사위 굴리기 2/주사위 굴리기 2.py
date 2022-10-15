from collections import deque

n, m, k = map(int,input().split())

maps = []

for i in range(n):
    maps.append(list(map(int,input().split())))

# 숫자가 앞으로 보이도록 접기
dice = [0,3,4,5,2,1,6]

# 동남서북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x, y = 0, 0
dir = 0
ans = 0

for i in range(k):
    
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        dir = (dir + 2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    
    east, west, south, north, up, down = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    
    if dir == 0 :
        dice[1], dice[2], dice[5], dice[6] = up, down, west, east
    elif dir == 1:
        dice[3], dice[4], dice[5], dice[6] = up, down, north, south
    elif dir == 2:
        dice[1], dice[2], dice[5], dice[6] = down, up, east, west
    elif dir == 3:  
        dice[3], dice[4], dice[5], dice[6] = down, up, south, north

    score = maps[nx][ny]

    if dice[6] > score:
        dir = (dir + 1) % 4
        
    elif dice[6] < score:
        dir = (dir - 1) % 4
    else:
        pass
        
    x, y = nx, ny

    visited = [[False] * m for _ in range(n)]
    
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    cnt = 1

    while que:
            
        x1, y1= que.popleft()

        for j in range(4):
            
            nx1 = x1 + dx[j]
            ny1 = y1 + dy[j]

            if nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m:
                continue
                
            else:
                   
                if maps[nx1][ny1] == score and visited[nx1][ny1] != True:
                    cnt += 1
                    que.append((nx1,ny1))
                    visited[nx1][ny1] = True
         
    ans += cnt * score

print(ans)
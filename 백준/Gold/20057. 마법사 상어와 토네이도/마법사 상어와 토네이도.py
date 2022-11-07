n = int(input())
sand = []
for i in range(n):
    sand.append(list(map(int,input().split())))

ans = 0
x,y = n//2, n//2

# 좌하우상
dx = [0,1,0,-1]
dy = [-1,0,1,0]

dir = 0

visited = [[False] * n for _ in range(n)]

# 회전했을 때 모래 퍼지는 비율 방향따라 다르게
windx = [
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]
windy = [
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
]
rate = [1,1,2,2,5,7,7,10,10]


def move_tonado(x,y):
    visited[x][y] = True
    dir = 0

    while True:
        if x == 0 and y == 0:
            break

        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] != True:
                visited[nx][ny] = True
                x,y = nx,ny
                move_sand(x,y,dir)
                dir = (dir + 1) % 4
                continue
            else:
                dir = (dir - 1) % 4
                continue
                

def move_sand(x,y,dir):
    # 격자밖으로 나간 모래
    global ans 
    temp = 0

    for i in range(len(rate)):

        nx = x + windx[dir][i]
        ny = y + windy[dir][i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            # 남은 모래의 양 구하기
            temp += (rate[i] * sand[x][y]) // 100
            ans += (rate[i] * sand[x][y]) // 100

        else:
            # 소수점 아래 버림
            sand[nx][ny] += (rate[i] * sand[x][y]) // 100
            temp += (rate[i] * sand[x][y]) // 100

    a = sand[x][y] - temp

    nx1 = x + dx[dir]
    ny1 = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < n:
        sand[nx1][ny1] += a
    else:
        ans += a

    # 모든 모래가 이동하므로
    sand[x][y] = 0
    
move_tonado(x,y)
print(ans)


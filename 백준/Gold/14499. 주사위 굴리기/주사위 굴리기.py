n, m, x, y, k = map(int,input().split())

map1 = []
for i in range(n):
    map1.append(list(map(int,input().split())))

command = list(map(int,input().split()))
dice = [0] * 6

# 동서북남
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

for i in command:
    # print(i)
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
        # 움직이는 면이 위에 오도록 동쪽이면 동쪽면이 위에 

        east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
        
        if i == 1 :
            dice[4], dice[5], dice[0], dice[1] = east, west, down, up
        elif i == 2:
            dice[4], dice[5], dice[0], dice[1] = west, east, up, down
        elif i == 3:
            dice[4], dice[5], dice[2], dice[3] = north, south, up, down
        elif i == 4:
            dice[4], dice[5], dice[2], dice[3] = south, north, down, up

        if map1[nx][ny] == 0:
            map1[nx][ny] = dice[5]
        else:
            dice[5] = map1[nx][ny]
            map1[nx][ny] = 0

    
        x, y = nx, ny 
        print(dice[4])
    
    else:
        continue
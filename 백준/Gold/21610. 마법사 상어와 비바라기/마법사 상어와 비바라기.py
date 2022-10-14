n, m = map(int,input().split())
basket = []
water = []

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

dx1 = [-1,-1,1,1]
dy1 = [-1,1,-1,1]

for i in range(n):
    basket.append(list(map(int,input().split())))

for i in range(m):
    water.append(list(map(int,input().split())))

cloud = [[n-2,0],[n-2,1],[n-1,0],[n-1,1]]

for d,s in water:
    
    temp = []
    # 구름 이동 - 1
    for x,y in cloud:
        nx = (x + dx[d] * (s)) % n
        ny = (y + dy[d] * (s)) % n

        # 바구니 물 증가 - 2
        basket[nx][ny] += 1
        temp.append((nx,ny))

 
    # 물복사 마법 시전 - 4
    for x,y in temp:
        for i in range(4):
            nx = x + dx1[i]
            ny = y + dy1[i]

            if 0 <= nx < n and 0 <= ny < n:
                if basket[nx][ny] >= 1 :
                   basket[x][y] += 1
    
    temp2 = []
    for i in range(n):
        for j in range(n):
            if (i,j) not in temp and basket[i][j] >= 2:
                basket[i][j] -= 2
                temp2.append((i,j))

    cloud = temp2

ans = 0
for i in range(n):
    for j in range(n):
        ans += basket[i][j]

print(ans)


from copy import deepcopy

n, m, k = map(int,input().split())
fireball = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    r,c,m,s,d = map(int,input().split())
    fireball[r-1][c-1].append([m,s,d])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for i in range(k):

    new_fireball = [[[] for _ in range(n)] for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            
            if len(fireball[x][y]) >= 1 :
               
                for i in fireball[x][y] : 
                  
                    d = i[2]
                    s = i[1]
                    m = i[0]

                    nx = (x + dx[d] * s) % n
                    ny = (y + dy[d] * s) % n

                    new_fireball[nx][ny].append([m,s,d])
            
    fireball = deepcopy(new_fireball)

    for x in range(n):
        for y in range(n):

            if len(fireball[x][y]) >  1:

                sum_m = 0
                sum_s = 0
                sum_dir = []
                arr_len = len(fireball[x][y])

                for i in fireball[x][y]:
                    sum_m += i[0]
                    sum_s += i[1]
                    sum_dir.append(i[2])

                even = 0
                odd = 0
                for i in sum_dir:
                    if i % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                if even == len(sum_dir) or odd == len(sum_dir):
                    start = 0
                else:
                    start = 1

                fireball[x][y] = []

                new_m = sum_m // 5
                new_s = sum_s // arr_len

                if new_m != 0:

                    for i in range(4):
                        fireball[x][y].append([new_m,new_s,start+(i*2)])
ans = 0

for i in range(n):
    for j in range(n):
        if len(fireball[i][j]) >= 1:
            
            for k in fireball[i][j]:
                ans += k[0]

print(ans)

                
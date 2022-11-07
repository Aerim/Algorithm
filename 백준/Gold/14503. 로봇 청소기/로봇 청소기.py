n, m = map(int,input().split())
r,c,dir = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr[r][c] = 2
cnt = 1

# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    flag = False

    for i in range(4):
        nr = r + dx[(dir+3) % 4]
        nc = c + dy[(dir+3) % 4]
        dir = (dir+3) % 4

        if 0 <= nr < n and 0<= nc < m:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 2
                r = nr
                c = nc
                flag = True
                cnt += 1
                break

    if not flag:
        nr = r - dx[dir]
        nc = c - dy[dir]

        if 0 <= nr < n and 0<= nc < m:
            if arr[nr][nc] == 1:
                print(cnt)
                break

            else:
                r = nr
                c = nc

        
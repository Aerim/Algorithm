# 번호가 낮은 바이러스부터 증식

from collections import deque

n, k = map(int,input().split())
tmp_arr = []
answer = 0
# 바이러스 종류 저장
virus_arr = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    tmp_arr.append(list(map(int,input().split())))
    for j in range(n):
        if tmp_arr[i][j] != 0:
            virus_arr.append((tmp_arr[i][j],i,j,0))
            
virus_arr.sort()
s,_x,_y = map(int,input().split())

que = deque(virus_arr)

while que:

    virus, x, y, time = que.popleft()
    
    if time == s:
        break
    
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if tmp_arr[nx][ny] == 0:
            tmp_arr[nx][ny] = virus
            time += 1
            que.append((virus,nx,ny,time))
            
            
print(tmp_arr[_x-1][_y-1])
# 벽 세우고 -> 바이러스 퍼뜨리기
import copy
from collections import deque

n, m = map(int,input().split())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]
    
# 벽 세우기
def wall(x):
    if x == 3:
        # 벽 3개 다 세우면 bfs로 바이러스 퍼뜨리기
        bfs()
        return 
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    wall(x+1)
                    # 원복
                    arr[i][j] = 0
                    
# 바이러스 퍼뜨리기      
def bfs():
    
    que = deque()
    tmp_arr = copy.deepcopy(arr)
    
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 2:
                que.append((i,j))
                
    while que:
        x,y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
       
            if tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                # 얘도 바이러스 감염됐으니까 또 퍼뜨릴려면 큐에 넣어서 bfs 
                que.append((nx,ny))
                
    global answer
    cnt = 0
    
    for i in range(n):
        cnt += tmp_arr[i].count(0)
        
    answer = max(answer,cnt) 
    
answer = 0
wall(0)
print(answer)
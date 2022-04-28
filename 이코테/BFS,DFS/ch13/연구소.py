# 안전 영역 최댓값 
from collections import deque
import copy

n, m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]   

def bfs():
    que = deque()
    
    tmp_arr = copy.deepcopy(arr)
    
    for i in range(n):
        for j in range(m):
            # 바이러스 퍼뜨려야 하니까 바이러스 있는 인덱스를 넣어서 큐에 넣기
            if tmp_arr[i][j] == 2:
                que.append((i,j))

    while que:
        x,y = que.popleft()
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
           
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
    
            if tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                # 바이러스 퍼뜨렸으니까 얘도 다시 퍼뜨리려면 큐에 넣어야함
                que.append((nx,ny))
                
    global answer 
    
    cnt = 0
    for i in range(n):
        cnt += tmp_arr[i].count(0)
        
    answer = max(answer,cnt)
    
    
# 벽 세우기 - 이 많은 경우의 수를 어떻게? -> 재귀로!
def wall(x):
    # 벽의 개수가 3개가 되면 바이러스 퍼뜨리기
    if x == 3:
        bfs()
        return 
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    # 벽 세우기
                    arr[i][j] = 1
                    wall(x+1)
                    arr[i][j] = 0

answer = 0
wall(0)
print(answer)


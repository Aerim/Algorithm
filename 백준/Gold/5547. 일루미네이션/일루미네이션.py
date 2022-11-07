# 육각형 관련 탐색 문제는 외곽 감싸기
# 흰색 부분을 탐색하여 회색 건물에 둘러쌓인 흰색 부분 탐색 x

from collections import deque

w, h = map(int,input().split())

arr = [[0 for _ in range(w+2)] for _ in range(h+2)]
visited = [[False for _ in range(w+2)] for _ in range(h+2)]

for i in range(1,h+1):
    arr[i][1:w+1] = map(int,input().split())

dx = [[-1,0,-1,1,-1,0],[1,0,1,-1,0,1]]
dy = [-1,-1,0,0,1,1]

def bfs(j,i):

    cnt = 0

    que = deque()
    que.append((j,i))
    visited[j][i] = True

    while que:

        y, x = que.popleft()

        for i in range(6):

            ny = y + dy[i]
            nx = x + dx[y % 2][i] 

            if nx < 0 or nx >= w + 2 or ny < 0 or ny >= h + 2:
                continue

            elif arr[ny][nx] == 0 and visited[ny][nx] == False:
                visited[ny][nx] = True
                que.append((ny,nx))

            elif arr[ny][nx] == 1:
                cnt += 1

    return cnt

print(bfs(0,0))
               


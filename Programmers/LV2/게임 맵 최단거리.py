from collections import deque

def bfs(maps,x,y):

    que = deque()
    que.append((x,y))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:

        _x, _y = que.popleft()

        for i in range(4):

            nx = _x + dx[i]
            ny = _y + dy[i]

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] += maps[_x][_y]
                que.append((nx,ny))

def solution(maps):

    bfs(maps,0,0)

    x,y = len(maps), len(maps[0])

    # 모두 1인경우는 주어지지 않으니까
    return -1 if maps[x-1][y-1] <= 1 else maps[x-1][y-1]
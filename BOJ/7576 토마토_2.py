from collections import deque

n, m = map(int, input().split())
graph = []

que = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(m):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if graph[i][j] == 1:
            que.append((i, j))

def bfs():

    while que:

        x, y = que.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

bfs()

res = 0

for i in range(m):
    for j in range(n):

        if graph[i][j] == 0:
            print(-1)
            exit()

        res = max(res,graph[i][j])

if res == 1:
    print(0)
else : print(res - 1)
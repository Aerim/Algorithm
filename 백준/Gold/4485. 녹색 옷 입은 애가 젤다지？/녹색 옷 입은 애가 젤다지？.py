import heapq

dx = [1,-1,0,0]
dy = [0,0,-1,1]

INF = 1e9
ans = []

def diskstra(x,y):

        que = []
        heapq.heappush(que,(graph[x][y],x,y))
        distance[x][y] = graph[x][y]

        while que:

            dist, x_node, y_node = heapq.heappop(que)

            for i in range(4):

                nx = x_node + dx[i]
                ny = y_node + dy[i]

                if nx < 0 or nx >= n  or ny < 0 or ny >= n:
                    continue

                if dist + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = dist + graph[nx][ny] 
                    heapq.heappush(que,(dist + graph[nx][ny],nx,ny))

        return distance[n-1][n-1]

while True:
    n = int(input())

    if n == 0:
        break
    
    graph = []
    distance = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        graph.append(list(map(int,input().split())))
    
    ans.append(diskstra(0,0))


for i in range(len(ans)):
    print("Problem " + str(i+1) + ": " + str(ans[i]))

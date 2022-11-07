n = int(input())
m = int(input())

INF = 1e9
graph = [[ INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j :
            graph[i][j] = 0
            
for i in range(m):
    a, b, c = map(int,input().split())
    
    graph[a][b] = min(graph[a][b], c)
    
# 시작점과 끝점이 정점을 거쳐가는 경우 계산
def floyd_warshall():
    
    # 거치는 정점
    for k in range(1,n+1): 
        # 시작점
        for i in range(1,n+1):
            # 종점
            for j in range(1,n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
floyd_warshall()
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
            
for i in range(1,n+1):
    print(*graph[i][1:])

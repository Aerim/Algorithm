# 다익스트라 : 한 정점에서 최단거리
# 플로이드 워셜  : 모든 정점에서의 최단거리

n, m, r = map(int,input().split())

INF = 1e9

item = list(map(int,input().split()))

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for i in range(r):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
    
def floyd_warshall():
    
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if graph[i][j] > graph[i][k] + graph[k][j] :
                    graph[i][j] = graph[i][k] + graph[k][j]

floyd_warshall()

ans = []

# 아이템의 최대 개수 - 낙하지점이 고정된 것이 아니므로 반복문으로 낙하지점마다의 최대 아이템 개수 계산
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        if graph[i][j] <= m:
            temp += item[j-1]
            
    else:
        ans.append(temp)
        

print(max(ans))
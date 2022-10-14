# 다익스트라 - 각각의 최단 경로

import heapq 

INF = 1e9
n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    fr, to , weight = map(int,input().split())
    
    graph[fr].append([to,weight])
    graph[to].append([fr,weight])

v1, v2 = map(int,input().split())

def dijkstra(s):
    
    distance = [INF for _ in range(n+1)]
    que = []
    heapq.heappush(que,(0,s))
    distance[s] = 0
    
    while que:
        
        dist, now = heapq.heappop(que)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(que,(dist + i[1], i[0]))
                
    
    return distance
                  
# 1 -> v1 -> v2 -> n : a
# 1 -> v2 -> v1 -> n : b

path1 = dijkstra(1)
path2 = dijkstra(v1)
path3 = dijkstra(v2)

a = path1[v1] + path2[v2] + path3[n]
b = path1[v2] + path3[v1] + path2[n]

if min(a,b) < INF:
    print(min(a,b))
else:
    print(-1)
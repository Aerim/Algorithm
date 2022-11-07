import heapq

INF = 1e9

n = int(input())
# 간선개수
m = int(input()) 

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for i in range(m):
    a, b, weight = map(int,input().split())
    graph[a].append([b,weight])
    
srt, fin = map(int,input().split())

def dijkstra(s):
    
    que = []
    distance[s] = 0
    heapq.heappush(que,[0,s])
    
    while que:
        
        dist, node = heapq.heappop(que)
        
        if distance[node] < dist:
            continue
        
        for i in graph[node]:
            
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(que,(dist + i[1], i[0]))
                

dijkstra(srt)

print(distance[fin])
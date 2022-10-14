#다익스트라
from dis import dis
import heapq

INF = 1e9

v, e = map(int,input().split())
start = int(input())

graph = [[] for _ in range(v+1)]

# 최단거리 저장 배열 무한대로 초기화
distance = [INF for _ in range(v+1)]

for i in range(e):
    fr, to,weight = map(int,input().split())

    graph[fr].append([to,weight])

# 방문하지 않은 노드 중 최단거리 짧은 노드 선택
# 최단 거리 저장 배열 갱신

def dijkstra(s):
    
    que = []
    
    # 방문하지 않은 노드 중 입력된 거리가 가장 짧은 노드 선택 -> heapq
    # 예를들어 1번 노드 방문 후 1번 노드와 연결된 노드 중에서 가장 짧은 노드 선택
    heapq.heappush(que,(0,s))
    
    # 자기 자신은 0으로 설정
    distance[s] = 0
    
    while que:
        
        dist, node = heapq.heappop(que)

        if distance[node] < dist:
            continue
        
        for i in graph[node]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(que,(dist+i[1],i[0]))
                
                
dijkstra(start)

for i in range(1,v+1):
    if distance[i] == 1e9:
        print('INF')
    else: print(distance[i])
    
    
    
 
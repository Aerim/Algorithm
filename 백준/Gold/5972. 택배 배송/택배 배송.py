import heapq

n, m = map(int,input().split())

INF = 1e9

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
def dijkstra(s):

    que = []
    heapq.heappush(que,(0,s))
    distance[s] = 0

    while que:

        dist, node = heapq.heappop(que)

        if dist < distance[node] :
            continue

        for new_node, new_cost in graph[node]:

            if dist + new_cost < distance[new_node]:
                distance[new_node] = dist + new_cost
                heapq.heappush(que,(dist + new_cost, new_node))

dijkstra(1)
print(distance[n])

import heapq

INF = 1e9

n = int(input())
m = int(input())

distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
path = [-1 for _ in range(n+1)]

for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])

v1,v2 = map(int,input().split())

def dijkstra(s):

  que = []
  heapq.heappush(que,(0,s))
  distance[s] = 0

  while que:

    dist, now = heapq.heappop(que)
    
    if dist > distance[now]:
      continue

    for i in graph[now]:
      if dist + i[1] < distance[i[0]]:
        distance[i[0]] = dist + i[1]
        heapq.heappush(que,(dist + i[1], i[0]))
        path[i[0]] = now

        
dijkstra(v1)
print(distance[v2])
path_result = [v2]
temp = v2

# 경로 역추적
while path[temp] != -1:
  path_result.append(path[temp])
  temp = path[temp]
  
print(len(path_result))

path_result.reverse()

print(*path_result)


# prim은 노드 중심으로 구함
# 인접한 노드 중에 가장 작은 간선을 선택하고, 방문한 노드는 선택x (순환제거)
import sys
import heapq
input = sys.stdin.readline

v, e = map(int,input().split())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for i in range(e):
    a, b, w = map(int,input().split())
    graph[a].append([w,b,a])
    graph[b].append([w,a,b])

def prim(graph, visited, start):
    visited[start] = True
    hq = graph[start]
    heapq.heapify(hq)

    answer = 0

    while hq:
        w, n1, n2 = heapq.heappop(hq)

        if not visited[n1] :
            visited[n1] = True
            answer += w

            for i in graph[n1]:
                if not visited[i[1]]:
                    heapq.heappush(hq,i)

    return answer 

print(prim(graph,visited,1))





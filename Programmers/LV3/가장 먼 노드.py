# 최단경로로 이동
from collections import deque

def bfs(s,distance,visited,edge):

    que = deque()
    que.append(s)

    visited[s] = True

    while que:

        p = que.popleft()

        for i in edge[p]:
            if visited[i] != True:
                que.append(i)
                visited[i] = True
                distance[i] = distance[p] + 1


def solution(n, edge):
    answer = 0

    edge = sorted(edge, key = lambda x : (x[0],x[1]))
    distance = [0] * (n+1)
    visited = [False] * (n+1)
    _edge = [[] for i in range(n+1)]

    for i in edge:
        _edge[i[0]].append(i[1])
        _edge[i[1]].append(i[0])

    bfs(1,distance,visited,_edge)

    answer = distance.count(max(distance))
    return answer
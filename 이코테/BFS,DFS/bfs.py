from collections import deque
from typing import Tuple

# BFS 메서드 정의
def bfs(graph, v, visited):

    # 큐에다가 처음 노드 넣기
    que = deque([v])

    #현재 노드 방문했다고
    visited[v]=True
   
    # 큐 원소 있으면
    while True:
        if not que: break

        # 큐에서 하나뽑아서 탐색
        v=que.popleft()  
        print(v,end="->")

        # 탐색
        for i in graph[v]:
            # 방문안했으면
            if not visited[i]:
                que.append(i)
                visited[i]=True

#각 노드가 연결된 정보를 list 자료형으로 펴햔(2차원 List)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 8],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 list 자료형으로 표현(1차원 List)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
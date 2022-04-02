# DFS 메서드 정의


def dfs(graph, v, visited):

    # 현재 노드가 없으면 넣어줌
    visited[v]=True

    print(v, end='->')

    # 인접 노드 탐색하기
    for i in graph[v]:
        # 탐색
         if not visited[i]:
            dfs(graph,i,visited)

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

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

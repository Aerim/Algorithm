# 노드 수 - 간선 수 = 네트워크 수
def dfs(v,computers,visited):
    visited[v] = True
    
    for i in range(len(computers)):
        if visited[i] == False and computers[v][i] == 1:
            visited[i] = True
            dfs(i,computers,visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(len(computers)):
        if visited[i] == False:
            dfs(i,computers,visited)
            answer += 1
            
    return answer
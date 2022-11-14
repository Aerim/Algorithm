def solution(m, n, puddles):
    answer = 0
    
    graph = [[1] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        graph[i][0] = 0
    for j in range(m + 1):
        graph[0][j] = 0
        
    for x, y in puddles:
        graph[y][x] = 0
        
    graph[1][1] = 1
 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            
            if graph[i][j] != 0:
                graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1000000007
            
    return graph[n][m]
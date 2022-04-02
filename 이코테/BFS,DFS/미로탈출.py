from collections import deque

n,m = list(map(int,input().split()))

arr = []
for i in range(0,n):
    arr.append(list(map(int,input())))

visited = [[False] * m for _ in range(n)]

x,y = 0,0

move = [[0,1],[0,-1],[1,0],[-1,0]]

# 최단거리를 구하는 것이므로 bfs사용
# 가까운 것부터 방문하기 때문에
def bfs(x,y,arr,visited):

    now = [x,y]
    queue = deque([now])

    # 현재 노드 방문함
    visited[x][y] = True

    while queue:

        temp = queue.popleft()

        for i in range(len(move)):
            
            # 이동
            nx = temp[0] + move[i][0] 
            ny = temp[1] + move[i][1] 
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                pass

            else:
                # 방문하지 않았고 괴물이 없는 경우
                if visited[nx][ny] == False and arr[nx][ny] == True:

                    # 제일 작은 칸의 수를 세기 위해 지나온 칸들의 갯수를 계속 더함
                    arr[nx][ny] = arr[temp[0]][temp[1]] + 1
                    visited[nx][ny] = True
                    queue.append([nx,ny])

    # n,m에서 미로를 무조건 탈출하니까
    return arr[n-1][m-1]             

print(bfs(x,y,arr,visited))
print(arr)
from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])

        dx = [-1, 1, 0 , 0]
        dy = [0, 0 , -1 ,1]

        result = [[-1 for _ in range(n)] for _ in range(m)]
        que = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i,j))
                    result[i][j] = 0   
        
        while que:
            x, y = que.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if result[nx][ny] == -1:
                    que.append((nx,ny))
                    result[nx][ny] = result[x][y] + 1

        return result
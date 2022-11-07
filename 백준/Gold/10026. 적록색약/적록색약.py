from collections import deque
import sys

input = sys.stdin.readline

graph = []
ans = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())

for i in range(n):
    temp = input().rstrip()
    temp_arr = []
    for j in temp:
        temp_arr.append(j)

    graph.append(temp_arr)

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

cnt1 = 0
cnt2 = 0

# 적록색약 아닌 사람
def not_jrpeople(i,j,v):

    que1 = deque()
    que1.append((i,j))
    visited1[i][j] = True

    while que1:

        x, y = que1.popleft()

        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited1[nx][ny] != True and graph[nx][ny] == v:
                    visited1[nx][ny] = True
                    que1.append((nx,ny))

def jr_people(i,j,v):

    que2 = deque()
    que2.append((i,j))
    visited2[i][j] = True

    while que2:

        x, y = que2.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:

                if v == 'R' or v == 'G':
                    if visited2[nx][ny] != True and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                        visited2[nx][ny] = True
                        que2.append((nx,ny))

                else:
                    if visited2[nx][ny] != True and graph[nx][ny] == v:
                        visited2[nx][ny] = True
                        que2.append((nx,ny))


for i in range(n):
    for j in range(n):
        if visited1[i][j] != True:
            not_jrpeople(i,j,graph[i][j])
            cnt1 += 1
        if visited2[i][j] != True:
            jr_people(i,j,graph[i][j])
            cnt2 += 1

print(cnt1, cnt2)

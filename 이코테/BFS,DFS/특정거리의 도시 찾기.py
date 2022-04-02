from collections import deque

n,m,k,x = list(map(int,input().split()))

# 가중치는 모두 1임에 주의
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
weight = [0] * (n+1)

# 노드 개수만큼 인접리스트 생성
for i in range(m):
    q,w=map(int,input().split())

    adj[q].append(w)

def bfs(v,adj):

    queue = deque([v])
    visited[v] = True

    while queue:

        v = queue.popleft()

        for j in adj[v]:

            # 이전 노드의 가중치에 +1 더하기 - 중요
            if not visited[j] and weight[j] == 0:
                visited[j] = True
                weight[j] = weight[v]+1
                queue.append(j)
               
bfs(x,adj)
answer = []

# 있을때 for문 돌리기

for i in range(1,len(weight)):
  
    if k == weight[i]:
        answer.append(i)
        print(i)

if not answer:
    print(-1)

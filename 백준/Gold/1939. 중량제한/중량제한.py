import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

fr, to = map(int,input().split())

start = 1
end = int(1e9)

def bfs(mid):
    
    visited = set()
    que = deque()
    que.append(fr)
    visited.add(fr)
     
    while que:
        
        p = que.popleft()
        
        for a,b in graph[p]:
            # 갈 수 있는 다리면서 이분탐색 mid중량값이 다리 중량 제한에 걸리지 않을 때
            if a not in visited and b >= mid:
                que.append(a)
                visited.add(a)
                
    return True if to in visited else False
            
ans = 1
while start <= end:
    
    mid = (start+end) // 2
  
    if bfs(mid) == False:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
               
print(ans)
# 최소 단계
from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    que = deque()
    # depth - 0
    que.append((begin,0))
    
    visited = [0 for i in range(len(words))]
    
    while que:
        q, depth = que.popleft()
        
        # bfs로 현재글자와 한글자 차이나는 것들을 que에 넣기
        # depth로 기억해서 que에 target이 들어가 있는 경우 찾기
        for w in range(len(words)):
            
            if q == target:
                return depth
            
            temp = 0
            
            for j in range(len(words[w])):
                if words[w][j] != q[j]:
                    temp += 1
                    
            if temp == 1 and visited[w] != 1:
                que.append((words[w],depth + 1))
                visited[w] = 1
                answer += 1
    return answer
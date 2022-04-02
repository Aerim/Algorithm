from collections import deque

def solution(priorities, location):
    answer = 0
    
    que = deque([])
    
    for i in range(len(priorities)):
        que.append([i,priorities[i]])
    
    while que:
        m = max(que,key = lambda x : x[1])
        answer += 1
        
        if m[0] == location:
            break
            
        i = que.index(m)
        que.remove(m)
        que.rotate(-(i))
        
    return answer
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    arr = []
    
    for s in skill_trees:
        
        que = deque(skill)
        temp = ''
        
        for j in s:
            if j in que and j == que[0]:
                que.popleft()
                temp += j
            elif j in que and j != que[0]:
                break
        else:
        
            if temp in skill:
                answer += 1
            
    return answer
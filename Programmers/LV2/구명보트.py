# 2명씩 밖에 못 탐
# 최소 경우의 수를 구해야 하니까 최솟값+최댓값 식으로 구하기
# 최소+최소 짝 2개씩 묶어서 구하면 최소 경우의 수를 구하지 x
from collections import deque

def solution(people, limit):
    answer = 0
    
    people = sorted(people)
    que = deque(people)
    
    rescue = []
    
    while que:
        
        if len(que) >= 2:
            if que[0] + que[-1] <= limit:
                p = que.pop()
                q = que.popleft()
                rescue.append([p,q])
            else:    
                p = que.pop()
                rescue.append([p])
        else:
            p = que.popleft()
            rescue.append([p])
            
    return len(rescue)
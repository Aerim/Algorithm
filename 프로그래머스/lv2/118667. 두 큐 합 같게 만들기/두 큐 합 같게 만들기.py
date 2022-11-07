from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    target = (sum1 + sum2) // 2
        
    len_queue1 = len(queue1)
        
    if sum1 == target and sum2 > target:
        return -1
    elif sum1 > target and sum2 == target:
        return -1
    
    while True:
        if sum1 == target and sum2 == target:
            break
    
        if sum1 > target :
           
            if queue1:

                temp = queue1.popleft()
                sum1 -= temp
                sum2 += temp
                queue2.append(temp)
            
        elif sum2 > target :
           
            if queue2:
                temp = queue2.popleft()
                sum1 += temp
                sum2 -= temp
                queue1.append(temp)
                
        # 두 큐 최대 길이만큼 탐색
        if answer >= 600000:
            return -1
            
        answer += 1
           
    return answer
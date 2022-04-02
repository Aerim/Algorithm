from collections import deque

def solution(progresses, speeds):
    answer = []
    pq = deque([])
  
    for i in range(len(progresses)):    
        
        if (100 - progresses[i]) % speeds[i] != 0:
            pq.append((100-progresses[i])//speeds[i] + 1)
            
        else:
            pq.append((100-progresses[i])//speeds[i])
    
    p = pq.popleft()
    count = 1
    
    while pq:
        
        # 뒤 기능이 먼저 개발 됨
        if p >= pq[0]:
            count += 1
            
            # 마지막일때
            if len(pq) == 1:
                answer.append(count)
                
            pq.popleft()
            
        # 앞기능 먼저 배포 
        else :
            
            # 마지막일때
            if len(pq) == 1:
                # 이전까지의 카운트 넣어줘야함
                answer.append(count)
                count = 1
                answer.append(count)
            else:
                answer.append(count)
                count = 1
                
            p = pq.popleft()
           
        
    return answers
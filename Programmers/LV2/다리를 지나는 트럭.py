# 효율성을 위해서 sum()대신 변수 사용

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    cnt = deque([0 for i in range(bridge_length)])
    truck_weights = deque(truck_weights)
    tot_weight = 0
   
    while cnt:
        
        answer += 1
        # cnt 맨 앞 인덱스에 0이 아닌 트럭이 오게 되면 다리 건너는 시간 만큼
        # 건너갔음을 의미, 각각 트럭에 대한 지나간 시간을 계산 안해도 됨
        p = cnt.popleft()
        
        if len(truck_weights) != 0:
            
            tot_weight -= p
            
            if tot_weight + truck_weights[0] <= weight:
                
                q = truck_weights.popleft()
                cnt.append(q)      
                tot_weight += q 
            else:
                cnt.append(0)
        
    return answer
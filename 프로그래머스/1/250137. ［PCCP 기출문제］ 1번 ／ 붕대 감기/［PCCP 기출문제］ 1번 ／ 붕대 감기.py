from collections import deque

def solution(bandage, health, attacks):
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    
    success = 0
    temp_health = health
    attacks = deque(attacks)
    max_time = attacks[-1][0]
     
    for i in range(1,(max_time + 1)):
        if i == attacks[0][0]:
            temp_health -= attacks[0][1]
                      
            attacks.popleft()
            success = 0 
            
        else:
            success += 1
            
            if success == t:
                temp_health = min(temp_health + y, health)
                success = 0
            
            temp_health = min(temp_health + x , health)   
        
        if temp_health <= 0 :
            return -1 
    answer = temp_health
    
   
    return answer
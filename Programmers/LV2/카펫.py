def solution(brown, yellow):
    answer = []
    
    for i in range(1,int((brown+yellow)**0.5)+1):
        if (brown+yellow) % i == 0:
            j = (brown+yellow) // i
            
            if (i*2) + (j-2)*2 + yellow == brown+yellow:
                answer.append(j)
                answer.append(i)
                break
        
    return answer
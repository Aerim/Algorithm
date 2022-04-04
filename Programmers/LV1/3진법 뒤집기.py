def solution(n):
    answer = 0
    
    threejin = []
    
    if n == 1:
        return 1
    
    while True:
        if n // 3  >= 3 :
        
            threejin.append(str(n%3))
            n = n//3
        
        else :
            threejin.append(str(n%3))
            threejin.append(str(n//3))
            break
        
    threejin = "".join(threejin)
    reversed(threejin)
    
    for i in range(len(threejin)):
        answer += int(threejin[i])*3**(len(threejin)-1-i)
    
    return answer
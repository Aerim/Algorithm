def solution(N, stages):
    answer = []
    
    dict = {x+1 : 0 for x in range(N)}
    
    stages = sorted(stages)
   
    cur = len(stages)
    
    for i in range(N):
        if stages.count(i+1):
            dict[i+1] = stages.count(i+1)/cur   
            cur = cur- stages.count(i+1)
          
    dict = sorted(dict.items(), key = lambda item : item[1], reverse = True)
    
 
    return [i[0] for i in dict]
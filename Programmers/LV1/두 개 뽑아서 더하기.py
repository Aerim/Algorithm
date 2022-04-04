from itertools import combinations

def solution(numbers):
    answer = []
    
    numbers.sort()

    combi = list(combinations(numbers,2))
    
    for i in range(len(combi)):
        sum = 0
        sum = combi[i][0] + combi[i][1]
        
        if sum not in answer:
            answer.append(sum)
        
    answer.sort()
    
    return answer
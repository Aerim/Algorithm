from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    # maxlen을 설정하면 설정된 길이 이상으로 원소가 들어올경우 맨 처음거 삭제시킴
    cache = deque(maxlen = cacheSize)
    
    for city in cities:
        
        c = city.upper()
        
        # hit
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        # miss
        else:
            cache.append(c)
            answer += 5
    
    return answer
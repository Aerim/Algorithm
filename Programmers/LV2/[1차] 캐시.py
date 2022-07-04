# 가장 오랫동안 참조되지 않은 페이지 교체
# 캐시의 크기는 한정적이기 때문에 자주 사용되는 데이터는 캐시에 남기고, 
# 자주 사용되지 않는 캐시는 삭제해서 제한된 리소스내에서 데이터를 빠르게 접근할 수 있게 합니다.
# hit - 캐시에 존재 
# miss - 캐시에 없음

def solution(cacheSize, cities):
    answer = 0
    
    # cache = [0] * cacheSize
    cache = []
    
    for city in cities:
        
        if len(cache) < cacheSize:
            # hit
            if city.upper() in cache:
                if len(cache) > 0:
                    idx = cache.index(city.upper())
                    cache.pop(idx)
                    cache.append(city.upper())
                answer += 1
            # miss
            elif city.upper() not in cache:
                if len(cache) + 1 <= cacheSize:
                    cache.append(city.upper())
                answer += 5
                    
        elif len(cache) == cacheSize:
            # hit
            if city.upper() in cache:
                idx = cache.index(city.upper())
                cache.pop(idx)
                cache.append(city.upper())
                answer += 1
            # miss
            elif city.upper() not in cache:
                if len(cache) > 0:
                    cache.pop(0)
                    cache.append(city.upper())
                answer += 5    
     
        
    return answer
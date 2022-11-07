import heapq

def solution(n, works):
    answer = 0
    hq = []
    _sum = sum(works)
    
    # heapify 시간복잡도 nlogn 그 외는 대부분 logn?
    for i in works:
        heapq.heappush(hq,-i)
    
    for i in range(1,n + 1):
        temp = heapq.heappop(hq)

        if _sum - 1 == 0:
            return 0
        
        heapq.heappush(hq,temp + 1)
        _sum -= 1
        
    else:
        for i in hq:
            answer += i * i
 
    return answer
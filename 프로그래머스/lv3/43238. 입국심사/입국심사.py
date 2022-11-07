def solution(n, times):
    answer = 0
    
    times = sorted(times)
    
    start = 1
    end = n * times[-1]
    
    while start <= end:
        mid = (start + end) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t
            
        # n보다 이상일 경우
        if cnt >= n:
            answer = mid
            end = mid - 1
            
        else:
            start = mid + 1
           
    return answer
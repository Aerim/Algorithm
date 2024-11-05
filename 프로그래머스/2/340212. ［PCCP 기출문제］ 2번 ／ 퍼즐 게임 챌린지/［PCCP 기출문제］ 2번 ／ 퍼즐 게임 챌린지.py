def solution(diffs, times, limit):
    answer = 100001
    
    start = 1
    end = 100001
    mid = 0
    
    while start<end: 
        mid = (start + end) // 2
        result = 0
        
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                result += times[i]
            else:
                temp = (times[i-1] + times[i]) * (diffs[i] - mid)
                result += temp 
                result += times[i]
        
        if result <= limit:
            end = mid 
            answer = min(mid, answer)
        elif result > limit:
            start = mid + 1
     	
    return answer
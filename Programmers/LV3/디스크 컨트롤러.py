import heapq

def solution(jobs):
    answer = 0
    
    j_len = len(jobs)
    jobs = sorted(jobs,key = lambda x : (x[0],x[1]))
    print(jobs)
    heap = []
    now = 0
    
    # 둘 중 하나라도 있으면 계속 반복문 돔
    # jobs이 다 빠져도 대기목록이 있을 수 있으니까
    while jobs or heap:
            
        # 작업 진행중에도 now보다 빨리 들어온 애들 넣어주기 - 대기목록
        while jobs:
            if jobs[0][0] <= now:
                k = jobs.pop(0)
                heapq.heappush(heap,[k[1],k[0]])
            else:
                break
    
        if heap:
            temp = heapq.heappop(heap)
            
            work_time = temp[0]
            request_time = temp[1]
            
            now += work_time
            
            # 요청부터 종료까지
            answer += now - request_time
         
        else:
            now += 1
    
    return answer // j_len

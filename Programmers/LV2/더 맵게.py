import heapq 
# heapq는 최소힙(작은값만을 찾아줌)- 코딩 테스트 문제 중 최솟값 , 혹은 최댓값을 계속해서 호출해야 하는 상황인 경우 Heap 구조를 이용하여 구현하면 시간측면에서 굉장히 효율적인 구현이 가능하다.

def solution(scoville, K):
    answer = 0
    temp = 0
    
    # 무한루프돌아야하니까
    heapq.heapify(scoville)
    
    while True:
        
        if scoville[0] >= K:
            break
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        temp = first + (second * 2)
        
        heapq.heappush(scoville, temp)
        answer += 1

    
    return answer
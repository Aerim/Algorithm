import heapq 

t = int(input())

for i in range(t):
    
    k = int(input())
    maxh = []
    minh = []
    visited = [False] * k

    for j in range(k):
    
        temp = input().split(' ')
        command, num = temp[0], int(temp[1])
       
        if command == 'I':

            heapq.heappush(maxh,(-num,j))
            heapq.heappush(minh,(num,j))
            visited[j] = True

        else:
        
            if num == -1:
                # 최솟값이 동기화 되지 않았을 경우 제거
                while minh and not visited[minh[0][1]]:
                        heapq.heappop(minh)

                if minh:
                    visited[minh[0][1]] = False
                    heapq.heappop(minh)
                        
            else:
                while maxh and not visited[maxh[0][1]]:
                        heapq.heappop(maxh)
                  
                if maxh:
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh)

    
    while minh and not visited[minh[0][1]]:
            heapq.heappop(minh)
    
    while maxh and not visited[maxh[0][1]]:
            heapq.heappop(maxh)

    if minh and maxh:
        print(-maxh[0][0], minh[0][0])
    else:
        print('EMPTY')                
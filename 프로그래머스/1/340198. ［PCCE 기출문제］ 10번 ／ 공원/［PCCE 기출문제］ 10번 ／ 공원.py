from collections import deque 

def solution(mats, park):
    
    answer = [-1]
    mats.sort(reverse = True)
    
    h = len(park)
    w = len(park[0])
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "-1":
                for m in mats:
                    if h-i < m or w-j < m:
                        continue
                    
                    cnt = 0
                    for x in range(i, i+m):
                        for y in range(j, j+m):
                            if park[x][y] == "-1":
                                cnt += 1
                    
                            if cnt == m * m:
                                answer.append(m)
    return max(answer)                     
            
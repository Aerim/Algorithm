# 같은 열 연속해서 밟을 수 없음
# dp - 과거에 구했던 해 이용 (메모이제이션)
# 총n행 4열
def solution(land):
    answer = 0
    
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
        land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])
    
    return max(land[-1])
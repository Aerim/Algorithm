n = int(input())
arr = list(map(int,input().split()))

# 최대 그룹 수 이니까 오름차순
# 내림차순 반례 5 5 1 1 1 
arr = sorted(arr)
answer = 0
cnt = 0

for i in range(n):
    # 현재 그룹안의 모험가 수
    cnt += 1
    
    # 모험가 수가 공포도보다 크거나 같으면
    if cnt >= i:
        cnt = 0
        answer += 1
        
print(answer)        
    
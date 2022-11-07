n, c = map(int,input().split())

arr = []

for i in range(n):
    arr.append(int(input()))
    
arr.sort()

start =1 
end = arr[-1] - arr[0]

# mid 보다 작으면 패스 크면 설치
# 설치 개수가 c보다 적으면 mid - 1 크면 mid + 1
# 설치하고 나면 그 설치된 노드가 기준이 됨을 유의
res = 0
def binary_search(arr,start,end):
    while start <= end:
        mid = (start + end) // 2
        
        cur = arr[0]
        cnt = 1
        
        for i in range(1,n):
            if arr[i] - cur >= mid :
                cnt += 1
                cur = arr[i]
        else:
            if cnt >= c :
                res = mid
                start = mid + 1 
                
            else:
                end = mid - 1

    return res

answer = binary_search(arr,start,end)
print(answer)
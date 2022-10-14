import sys
input = sys.stdin.readline

n, m, l = map(int,input().split())

arr = list(map(int,input().split()))

# 고속도로 끝에 휴게소 설치 안 됨
arr.append(0)
arr.append(l)
arr.sort()

left = 1
right = l - 1
res = 0

# a와 b사이에 mid 간격으로 몇개의 휴게소를 세울 수 있는지
def binary_search(arr,left,right):

    while left <= right:

        mid = (left + right) // 2
        cnt = 0

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > mid:
                # 이미 설치된 휴게소는 설치 안 되므로
                cnt += (arr[i] - arr[i-1] - 1) // mid

        else:
            if cnt > m:
                left = mid + 1

            else:
                res = mid
                right = mid - 1
    return res

ans = binary_search(arr,left,right)
print(ans)
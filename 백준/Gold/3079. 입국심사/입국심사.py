import sys
input = sys.stdin.readline

n, m = map(int,input().split())

arr = []

for i in range(n):
    arr.append(int(input()))

left = min(arr)
right = max(arr) * m

res = right

# 임의의 시간 동안 최대 몇 명이 심사받을 수 있는지, 이 값을 최소로 하자
while left <= right:

    mid = (right + left) // 2
    people = 0

    # i번 심사대에서 받을 수 있는 인원 수 구하기 
    for i in arr:
        people += mid // i

    else:
        # 입국심사 받은 사람이 더 많음
        if people >= m:
            res = min(mid, res)
            right = mid - 1

        else:
            left = mid + 1

print(res)

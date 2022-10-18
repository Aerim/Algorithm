import sys
input = sys.stdin.readline

n, s = map(int,input().split())
arr = sorted(list(map(int,input().split())))
cnt = 0

def back(idx,temp_sum):

    global cnt 

    if idx >= n:
        return 

    temp_sum += arr[idx]

    if temp_sum == s:
        cnt += 1

    back(idx + 1, temp_sum)

    back(idx + 1, temp_sum - arr[idx])

back(0,0)

print(cnt)
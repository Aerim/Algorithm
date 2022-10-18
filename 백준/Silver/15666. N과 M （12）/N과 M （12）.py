import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
ans = []
res = set()
temp = 0

def back(temp):
    if len(ans) == m:
        res.add(tuple(ans))
        return 

    for i in range(temp,n):
        ans.append(arr[i])
        temp = i
        back(temp)
        ans.pop()

back(temp)

for i in sorted(res):
    print(*i)



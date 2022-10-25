import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

ans = [0,0,0]
res = 1e10

for i in range(n-2):

    left = i + 1
    right = n - 1

    while left < right:

        temp = arr[i] + arr[left] + arr[right]

        if temp == 0:
            ans = [arr[i], arr[left], arr[right]]
            print(*ans)
            sys.exit(0)
        
        if abs(temp) < abs(res) :
            res = temp
            ans = [arr[i], arr[left], arr[right]]

        if temp < 0:
            left += 1
        
        elif temp > 0 :
            right -= 1


ans.sort()
print(*ans)

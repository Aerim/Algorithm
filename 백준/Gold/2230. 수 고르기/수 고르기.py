n, m = map(int,input().split())

arr = []

for i in range(n):
    arr.append(int(input()))
    
arr.sort()

ans = 2e9

l = 0 
r = 0

while l < n and r < n:
    
    diff = abs(arr[r] - arr[l])
    
    if diff >= m:
        if diff < ans:
            ans = diff    
        l += 1
    # diff < m
    else:
        r += 1
        
print(ans)
         
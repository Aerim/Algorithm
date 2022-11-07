n = int(input())

arr = list(map(int,input().split()))

l = 0
r = len(arr) - 1

ans = [arr[l],arr[r]]
diff = abs(arr[r] + arr[l])

while l < r :
    
    temp = abs(arr[l] + arr[r])
    
    if temp < diff:
        diff = temp
        ans = [arr[l],arr[r]]
        
    if arr[l] + arr[r] < 0:
        l += 1
    else:
        r -= 1
        
print(ans[0],ans[1])
        
        
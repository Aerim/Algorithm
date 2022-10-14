n = int(input())

arr = list(map(int,input().split()))
arr = sorted(arr)

l,r = 0, n-1
val = abs(arr[l] + arr[r])
ans = [arr[l], arr[r]]

while l < r:
  
  if abs(arr[l] + arr[r]) < val:
    val = abs(arr[l] + arr[r])
    ans = [arr[l], arr[r]]

  if arr[l] + arr[r] < 0:
    l += 1
  else:
    r -= 1

print(ans[0], ans[1])
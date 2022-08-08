n = int(input())

arr = list(map(int,input().split()))

stack = []
ans = []

for i in range(n):
  while stack:
    if stack[-1][1] > arr[i]:
      ans.append(stack[-1][0] + 1)
      stack.append((i,arr[i]))
      break
    else:
      stack.pop()
      
  if len(stack) == 0:
    stack.append((i,arr[i]))
    ans.append(0)

print(*ans)
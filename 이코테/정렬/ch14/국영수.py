# 내림차순은 람다 -로
n = int(input())

arr = []

for i in range(n):
    arr.append(list(input().split()))
    
arr = sorted(arr, key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(len(arr)):
    print(arr[i][0])
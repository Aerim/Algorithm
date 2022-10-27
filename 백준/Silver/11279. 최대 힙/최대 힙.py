import sys
import heapq

input = sys.stdin.readline
arr = []

for i in range(int(input())):
    x = int(input())

    if x > 0 :
        heapq.heappush(arr,(-x,x))
    else:
        if len(arr) == 0:
            print(0)
            continue
        else:
            print(arr[0][1])
            heapq.heappop(arr)


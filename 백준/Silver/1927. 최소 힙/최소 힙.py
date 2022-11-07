
import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    x = int(input())

    if len(arr) == 0 and x == 0 :
        print(0)
    else:
        if x > 0 :
            heapq.heappush(arr,x)

        elif x == 0:
            print(arr[0])
            heapq.heappop(arr)


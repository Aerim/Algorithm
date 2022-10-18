import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr1 = permutations(arr,n)
max_v = 0

for i in arr1:
    v = 0
    for j in range(1,n):
        v += abs(i[j-1] - i[j])

    max_v = max(max_v,v)

print(max_v)
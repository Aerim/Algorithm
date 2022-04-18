"""
5 8 3
2 4 5 4 6

"""

n , m , k =map(int,input().split())

arr = list(map(int,input().split()))

arr = sorted(arr)

print(arr[-1]*k*(m//k) + arr[-2]*(m%k))
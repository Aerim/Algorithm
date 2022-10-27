# 분할정복
import sys

input = sys.stdin.readline
n,r,c = map(int,input().split())

ans = 0

while 1:
    
    # 1사분면
    if r < (2 ** (n - 1)) and c < (2 ** (n - 1)):
        ans += (2 ** (n - 1) * (2 ** (n - 1))) * 0
    
    # 2사분면
    elif r < (2 ** (n - 1)) and c >= (2 ** (n - 1)):
        c -= 2 ** (n - 1)
        ans += (2 ** (n - 1) * (2 ** (n - 1))) * 1

    # 3사분면
    elif r >= (2 ** (n - 1)) and c < (2 ** (n - 1)):
        r -= 2 ** (n - 1)
        ans += (2 ** (n - 1) * (2 ** (n - 1))) * 2

    # 4사분면
    elif r >= (2 ** (n - 1)) and c >= (2 ** (n - 1)):
        r -= 2 ** (n - 1)
        c -= 2 ** (n - 1)
        ans += (2 ** (n - 1) * (2 ** (n - 1))) * 3

    n -= 1

    if n == 0:
        break
print(ans)
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

coins = sorted(coins, reverse = True)

ans = 0

for coin in coins:

    if coin <= k:
        ans += k // coin
        k = k - ((k // coin) * coin)
      
print(ans)

n, k = map(int,input().split())

coin = []

# dp[4] : 4원 만들 수 있는 경우의 수
dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in range(n):
    coin.append(int(input()))
    
# dp[4] 를 2원으로 만든다고 치면 4 - 2 = 2 : dp[2]
for c in coin:
    for i in range(c,k+1):
        dp[i] += dp[i-c]
        

print(dp[k])
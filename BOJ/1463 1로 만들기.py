# 연산 횟수의 최솟값
# dp - 큰 문제를 작은 문제로 쪼개고 이전 값들을 이용하자

n = int(input())

dp = [0] * (n+1)

for i in range(2,n+1):

    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
         dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

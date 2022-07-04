# 수를 1개 이상 사용해야함

t = int(input())
res = []

for i in range(t):
    
    n = int(input())

    dp = [0] * (n + 1) 

    for i in range(1,n+1):

        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    res.append(dp[n])

for i in range(len(res)):
    print(res[i])
    
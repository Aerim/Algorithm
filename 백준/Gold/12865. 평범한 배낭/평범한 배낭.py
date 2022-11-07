n, k = map(int,input().split())

arr = [[0,0]]

for i in range(n):
    arr.append(list(map(int,input().split())))
    
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w = arr[i][0]
        v = arr[i][1]
       
        if j < w:
           dp[i][j] = dp[i-1][j]
           
        else:
            # 현재 배낭에 무게를 넣으려면 현재 무게 - 무게 뺀 후 그때의 가치에 현재 가치 더하기
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w] + v)   
          
print(dp[n][k])  
        
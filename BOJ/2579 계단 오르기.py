# 한번에 한계단 혹은 두계단씩
# 연속된 세개의 계단 모두 밟으면 안됨
# 마지막 계단 무조건 밟기 

# 점수 최댓값

n = int(input())

st = []
# 최댓값 저장

for i in range(n):
    st.append(int(input()))

dp = []
dp.append(st[0])

if n == 1:
    print(st[0])
elif n == 2:
    print(st[0] + st[1])
elif n == 3:
    print(max(st[0] + st[2], st[1] + st[2]))
else:
    dp.append(st[0] + st[1])
    dp.append(max(st[0] + st[2], st[1] + st[2]))

    for  i in range(3,n):
        dp.append(max(dp[i-2] + st[i], dp[i-3] + st[i-1] + st[i]))

    else:
        print(dp[n-1])
import sys

input = sys.stdin.readline

r,c,q = map(int,input().split())
pic = []
arr = []
for i in range(r):
    pic.append(list(map(int,input().split())))

for i in range(q):
    arr.append(list(map(int,input().split())))

# 누적합
# 최악의 경우 100000(q) * 1000(r) * 1000(c) 이므로
sum_arr = [[0] * (c + 1) for _ in range(r + 1)]


for i in range(1,r+1):
    for j in range(1,c+1):
        sum_arr[i][j] = pic[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

for i in arr:
    r1,c1,r2,c2 = i[0],i[1],i[2],i[3]

    temp = sum_arr[r2][c2] - sum_arr[r2][c1-1] - sum_arr[r1-1][c2] + sum_arr[r1-1][c1-1]

    garo = abs(c1-c2) + 1
    sero = abs(r1-r2) + 1

    e_len = garo * sero
    print(temp // e_len )
import sys

input = sys.stdin.readline

t = int(input())
save_zero = [0] * (41)
save_one = [0] * (41)

save_zero[0] = 1
save_zero[1] = 0

save_one[0] = 0
save_one[1] = 1

for i in range(2,41):

    save_zero[i] = save_zero[i-1] + save_zero[i-2]
    save_one[i] = save_one[i-1] + save_one[i-2]


for i in range(t):

    n = int(input())

    print(save_zero[n], save_one[n])

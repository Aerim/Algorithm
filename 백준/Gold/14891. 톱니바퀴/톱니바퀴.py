from collections import deque

wheels = []
wheels_rotate = []
for i in range(4):
    wheels.append(deque(map(int,input())))

k = int(input())
for i in range(k):
    wheels_rotate.append(list(map(int,input().split())))

def chk_left(num,dir):

    if num - 1 < 0 or wheels[num][6] == wheels[num - 1][2]:
        return

    if wheels[num - 1][2] != wheels[num][6]:
        chk_left(num - 1, -dir)
        wheels[num - 1].rotate(-dir)
        

def chk_right(num,dir):

    if num + 1 >= 4 or wheels[num + 1][6] == wheels[num][2]:
        return

    if wheels[num + 1][6] != wheels[num][2]:
        chk_right(num + 1, -dir)
        wheels[num + 1].rotate(-dir)
    

# 1이면 시계-1이면 반시계 회전
# 방향이 같으면 회전하지 않음
for i in wheels_rotate:

    num = i[0] - 1
    dir = i[1]

    # 오른쪽 왼쪽 나눠서 각각 조사
    # 기준 톱니바퀴는 돌아가야 하기 때문에 빼고 조사
    chk_right(num ,dir)
    chk_left(num,dir)
    wheels[num].rotate(dir)

ans = 0

# n극은 0 s극은 1
for i in range(4):
    if i == 0 and wheels[i][0] == 1:
        ans += 1
    
    elif i == 1 and wheels[i][0] == 1:
        ans += 2
    
    elif i == 2 and wheels[i][0] == 1:
        ans += 4
    
    elif i == 3 and wheels[i][0] == 1:
        ans += 8

print(ans)




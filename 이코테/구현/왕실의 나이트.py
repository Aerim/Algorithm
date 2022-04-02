now = input()
count = 0 

x = int(now[1])

# x좌표 값 찾기 - 이 형태 잘 기억해놓자!
y =int(ord(now[0])) - int(ord('a')) + 1

# 나이트 움직임
move = [[2,-1], [2,1], [-2,-1], [-2,1], [1,2], [1,-2], [-1,2],[-1,-2]]

for i in range(len(move)):
    nx = x + move[i][0]
    ny = y + move[i][1]

    if nx <= 8 and ny <= 8 and nx > 0 and ny > 0 :
        count+=1

print(count)

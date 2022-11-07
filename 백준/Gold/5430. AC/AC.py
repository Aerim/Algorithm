import sys
from collections import deque

input = sys.stdin.readline

for i in range(int(input())):
    p = input().rstrip()
    n = int(input())
    temp = input().rstrip()

    if len(temp[1:-1]) > 0:
        que = deque(temp[1:-1].split(','))

    else:
        que = deque()

    r_cnt = 0
    flag = False

    for i in p:
        if i == 'R':
            r_cnt += 1

        elif i == 'D':
            if len(que) <= 0:
                flag = True
                break
            else:   
                if r_cnt % 2 == 1:
                    que.pop()
                elif r_cnt % 2 == 0:
                    que.popleft()

    if r_cnt % 2 == 1:
        que.reverse()

    if flag == False:
        print("["+",".join(list(que)) + "]")
    else:
        print('error')
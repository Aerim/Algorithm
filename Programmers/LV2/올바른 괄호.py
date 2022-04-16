from collections import deque

def solution(s):

    answer = True

    que = deque([])

    for i in s:
        if i == '(':
            que.append('(')

        elif i == ')':
            if len(que) != 0:
                que.popleft()
            else:
                return False

    else:
        if len(que) == 0:
            return True

        else: 
            return False

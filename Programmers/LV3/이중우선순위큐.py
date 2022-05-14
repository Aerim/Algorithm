from collections import deque
def solution(operations):
    answer = [0,0]
    que = deque([])

    for i in operations:
        op = i.split(' ')[0]
        num = int(i.split(' ')[1])

        if op == 'I':
            que.append(num)
        elif op == 'D':
            if num == -1:
                if len(que) != 0:
                    que = deque(sorted(que))
                    que.popleft()

            elif num == 1:
                if len(que) != 0:
                    que = deque(sorted(que, reverse = True))
                    que.popleft()

    if len(que) != 0:
        answer = [max(que),min(que)]
    return answer
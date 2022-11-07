# (()[[]])([]) = (()) + ([[]]) + ([]) =  2 * 2 + 2 * 3 *3 + 2 * 3
# 여는 괄호 값만큼 곱해진 값이 최종값에 더해져야 함 -> 최종 값 더한 후 닫는 괄호 만큼 나눠서 다시 구하자

import sys
input = sys.stdin.readline

string = input()

stack = []
ans = 0
temp = 1

for i in range(len(string)):
    if string[i] == '(':
        temp *= 2
        stack.append(string[i])

    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break

        if string[i-1] == '(':
            ans += temp
                
        temp //= 2
        stack.pop()


    elif string[i] == '[':
        temp *= 3
        stack.append('[')
    
    elif string[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
       
        if string[i-1] == '[':
            ans += temp
                
        temp //= 3
        stack.pop()

if len(stack) >= 1:
    print(0)
else: print(ans)
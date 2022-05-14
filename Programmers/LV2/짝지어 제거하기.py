def solution(s):
    
    arr = []
    temp = []
    
    # 스택을 하나 만들어서 맨 마지막 원소와 일치하면 pop 아니면 push
    for i in range(len(s)):
        if len(temp) == 0:
            temp.append(s[i])
        elif temp[-1] == s[i]:
            temp.pop()
        else:
            temp.append(s[i])
            
    if len(temp) == 0:
        return 1
    else:
        return 0
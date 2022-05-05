from collections import deque

def str_div(p):
    
    l = 0
    r = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        
        if l == r :
            return p[:i+1], p[i+1:]

def check_str(u):
    
    que = deque()
    
    for i in u:
        if i == '(':
            que.append('(')
        else:
            if len(que) != 0:
                que.pop()
    
    if len(que) != 0:
        return False
    else:
        return True
  
def recursive(p):
    
    if len(p) == 0:
        return ""
    
    u ,v = str_div(p)
    
    k = ''
    z = ''
    
    if check_str(u) == False:
        k += '('
        k += recursive(v)
        k += ')'
        
        for i in u[1:-1]:
            if i == '(':
                z += ')'
            else:
                z += '('
        return k + z
    
    else:
        return u + recursive(v)
        
def solution(p):
    answer = ''
    
    answer = recursive(p)
    
    return answer
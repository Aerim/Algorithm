def solution(p):
    answer = recursive(p)
    return ''.join(answer)

def recursive(v):
    count1 =0
    count2 =0
    u = []
    v= list(v)
    # 처음 균형잡힌 문자열 찾기
    for i in range(len(v)):
        if v[i] =="(":
            count1 += 1
        else:
            count2 += 1
        if count1 == count2:
            u = v[:i+1]
            v = v[i+1:]
            break
    # u 가 올바른지 아닌지를 판단한다. 
    checker =False 
    cnt = 0
    for i in u:
        # (이면 +1하고 아닐때 -1하면 올바른 문자열 아닐때 공백 추출가능
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            break
            checker= False
        else: 
            checker= True
    # u가 올바르지 않을때
    if checker == False:  
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(":
                u[i] =")"
            elif u[i] == ")":
                u[i] = "("

    if checker == False:
        # v가 공백
        if v ==[]:
            return ["(",")"]+u
        return ["("]+recursive(v)+[")"]+u
    if checker == True:
        # v가 공백이면 종료
        if v ==[]:
            return u
        return u + recursive(v)

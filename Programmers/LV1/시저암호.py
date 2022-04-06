def solution(s, n):

    up_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
               'X','Y','Z']
    do_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
               'x','y','z']

    str = ''
    idx = 0

    for i in range(len(s)):
        if s[i].isupper() == True:
            idx = up_alpha.index(s[i])

            if idx + n > 25:
                str += up_alpha[idx-25+(n-1)]
            else:
                str += up_alpha[idx+n]

        elif s[i].islower() == True:
            idx = do_alpha.index(s[i])  

            if idx + n > 25:
                str += do_alpha[idx-25+(n-1)]
            else:
                str += do_alpha[idx+n]
        else : 
            str += ' '

    answer = str
    return answer
def solution(s):
    answer = ''
    
    number = {'ze' : [0,2], 'on' : [1,1], 'tw' : [2,1], 'th' : [3,3], 'fo' : [4,2], 'fi' : [5,2],
             'si' : [6,1], 'se' : [7,3], 'ei' : [8,3], 'ni' : [9,2]}
    
    for i in range(len(s)):
        if s[i].isdigit() == True:
            answer += str(s[i])
        else:
            if i != len(s)-1 and s[i]+s[i+1] in number.keys():
                answer += str(number.get(s[i]+s[i+1])[0])
               
    return int(answer)
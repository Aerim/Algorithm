from collections import Counter
def solution(str1, str2):
    answer = 0
    
    d1 = Counter([str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha() == True])
    d2= Counter([str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha() == True])
    
    lam = lambda d1,d2 : 1 if len(d1) == 0 and len(d2) == 0 else sum((d1&d2).values()) / sum((d1|d2).values())
    
    answer = lam(d1,d2)
  
    return int(answer * 65536)
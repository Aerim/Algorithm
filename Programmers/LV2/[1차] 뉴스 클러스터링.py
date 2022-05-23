# 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눔
# 문자열은 두글자씩 끊어서 - 영문만
# 집합 a 집합 b 모두 공집합이면 1
from collections import Counter

def intersection(arr1,arr2):
    intersec = 0

    dict = Counter(arr1)
    dict1 = Counter(arr2)
    
    for k,v in dict.items():
        if k in dict1:
        
            intersec += min(dict[k],dict1[k])
    
    return intersec

def solution(str1, str2):
    answer = 0
    s1, s2 = [], []
    _s1, _s2 = [], []
    
    if len(str1) == 0 and len(str2) == 0:
        return 1 * 65536
    
    for i in str1:
        if i.isalpha() == True:
            s1.append(i.lower())
        else:
            s1.append(' ')
          
    for i in str2:
        if i.isalpha() == True:
            s2.append(i.lower())
        else:
            s2.append(' ')
            
    for i in range(len(s1)):
        if i + 1 < len(s1) and s1[i+1] != ' ' and s1[i] != ' ':
            temp = s1[i] + s1[i+1]
            _s1.append(temp)
    
    for i in range(len(s2)):
        if i + 1 < len(s2) and s2[i+1] != ' ' and s2[i] != ' ':
            temp = s2[i] + s2[i+1]
            _s2.append(temp)

    if len(_s1) == 0 and len(_s2) == 0:
        return 1 * 65536
    
    a = intersection(_s1,_s2)    
    
    b = len(_s1) + len(_s2) - a
    return int(a / b * 65536)
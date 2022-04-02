# 파이썬 hash는 딕셔너리로 구성
from itertools import combinations
from collections import Counter

def solution(clothes):
    answer = 1
    dict = {}
    
    arr = []
    
    for i,j in clothes:
        arr.append(j)
        
    cnt = Counter(arr)
    
    for i in cnt.values():
        answer *= i+1
        
#case1 - 시간초과 풀이
# answer = 0
    
#     dict = {}
#     arr = []
    
#     for i in clothes:
#         if i[1] not in dict:
#             dict[i[1]] = dict.get(i[1],1)
#         else:
#             dict[i[1]] += 1
      
#     arr = list(dict.values())

 
#     for i in range(1,len(arr)+1):
#         temp = list(combinations(arr,i))
#         num = 1
        
#         for j in temp:
#             for k in j:
#                 num = num * k
#             else:
#                 answer += num
#                 num = 1
               
    return answer - 1
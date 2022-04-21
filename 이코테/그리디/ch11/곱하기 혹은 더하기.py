s = str(input())

s = [i for i in s]
answer = int(s[0])

# 11111 - 케이스 고려 -> 5
for i in range(1,len(s)):
    
    if answer + int(s[i]) > answer * int(s[i]):
        answer += int(s[i])
        
    else:
        answer *= int(s[i])
   
print(answer)
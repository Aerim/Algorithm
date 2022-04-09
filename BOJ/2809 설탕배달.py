n = int(input())

answer = 0

while True:
    
    if n <= 0:
        break
    
    if n % 5 == 0:
        
        answer += n // 5 
        n = n % 5
    
    else :
        answer += 1
        n = n - 3
        

if n == 0:
    print(answer)
    
else:
    print(-1)
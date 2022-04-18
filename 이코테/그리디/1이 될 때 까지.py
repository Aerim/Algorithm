#효율성 생각 - 계속 1씩 빼는 것은 숫자가 커지면 빠르게 동작하지 않음 - 최대한 많은 숫자를 한번에 빼자

n , k = map(int,input().split())

answer = 0

while True:
    
    if n < k : 
        break
    
    if n % k != 0:
        minus = (n//k) * k
        answer += n - minus
        n = minus
    else:
        n = n // k 
        answer += 1

# 나눈 나머지가 1이 아니면 나머지에 대해 -1 , n = 1이면 0이 더해짐
print(answer + (n-1))
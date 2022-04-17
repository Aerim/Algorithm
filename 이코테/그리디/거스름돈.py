"""
1260 - 6
"""

n = int(input())

coin = [500,100,50,10]
answer = 0

for i in coin:
    answer += n // i
    n = n % i
    print(answer, n)

print(answer)
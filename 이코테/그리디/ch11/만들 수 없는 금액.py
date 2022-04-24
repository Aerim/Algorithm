"""
5
3 2 1 1 9

"""
# 꼭 동전 5개를 다 쓸 필요x
# coin이하의 수는 다 만들수 있다는 개념

n = int(input())
coin = list(map(int,input().split()))
coin = sorted(coin)

money = 1

for c in coin:
    if money < c:
        break
    
    money += c
    
print(money)


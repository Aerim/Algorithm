def solution(price, money, count):

    _sum = 0

    for i in range(1,count+1):
        _sum += i * price

    if _sum > money:
        return _sum - money
    else:
        return 0
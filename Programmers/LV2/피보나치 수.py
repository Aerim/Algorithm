# 재귀를 쓴다면 그 장점은 대표적으로 두가지다
# 1. 알고리즘을 재귀적으로 표현하는 것이 자연스러울 때
# 2. 변수 사용을 줄이기 위해

# 그렇다면 단점도 있을 것 같다.
# 1. 메모리를 많이 차지
# 2. 성능이 반복문에 비해 느리다

#dp사용
def solution(n):
    answer = 0

    memory = []

    for i in range(n+1):
        if i == 0 :
            memory.append(0)
        elif i == 1 :
            memory.append(1)
        else:
            memory.append(memory[i-1]+memory[i-2])

    return memory[n] % 1234567

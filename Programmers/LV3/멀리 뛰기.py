# 한번에 1칸 혹은 2칸만 이동 가능
# 규칙 찾아서 dp 사용

def solution(n):
    answer = 0

    arr = [0,1,2]

    for i in range(3,n+1):
        arr.append(arr[i-1] + arr[i-2])

    return arr[n] % 1234567
def solution(arr, divisor):
    answer = []

    for i in range(len(arr)):
        if arr[i] % divisor == 0 :
            answer.append(arr[i])

    return [-1] if len(answer) == 0 else sorted(answer)
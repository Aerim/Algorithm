def solution(arr):
    answer = []

    flag = False

    for i in range(len(arr)):
        if i != len(arr)-1 :
            if arr[i+1] != arr[i]:
                answer.append(arr[i])
        else:
            answer.append(arr[i])
    return answer
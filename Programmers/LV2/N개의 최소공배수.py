def solution(arr):

    gcd = arr[0]

    for i in range(1,len(arr)):
        temp = arr[i]
        while True:
            if temp % gcd == 0:
                gcd = temp
                break
            temp += arr[i]

    return gcd
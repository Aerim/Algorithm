def solution(n):
    answer = 0

    arr = [i for i in range(1,n+1)]

    for i in range(len(arr)):
        sum = arr[i]

        for j in range(i+1,len(arr)):
            sum += arr[j]

            if sum == n:
                answer += 1

                break
            elif sum > n:
                break

    return answer+1
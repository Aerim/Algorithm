def solution(s):
    answer = []
    arr = []

    arr = s[2:-2].split('},{')
    arr = sorted(arr, key = len)

    for i in arr:
        temp = i.split(',')
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))


    return answer
def solution(s):
    answer = []

    array = s.split(" ")

    for i in array:
        str = ''
        for j in range(len(i)):
            if j % 2 == 0:
                str += i[j].upper()
            else:
                str += i[j].lower()

        answer.append(str)

    return " ".join(answer)
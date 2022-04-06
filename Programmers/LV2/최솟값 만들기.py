def solution(A,B):
    answer = []

    A = sorted(A)
    B = sorted(B, reverse = True)

    for i in zip(A,B):

        answer.append(i[0] * i[1])

    return sum(answer)

def solution(dartResult):
    answer = 0

    score = {'S' : 1, 'D' : 2, 'T' : 3}
    option = ['*', '#']

    arr = []
    number = ''

    for i in enumerate(dartResult) :

        if i[1].isdigit() == True :
            print(i[1])
            number += i[1]     

        else:
            if i[1] in score :
                number = int(number)**score.get(i[1])
                arr.append(number)
                number = ''

            elif i[1] == option[0] :

                if len(arr) != 1 :
                    arr[-1] = arr[-1]*2
                    arr[-2] = arr[-2]*2
                else:
                    arr[-1] = arr[-1]*2
            else:
                arr[-1] = -arr[-1]

    return sum(arr)
def solution(s):

    arr = s.split(' ')
    arr1 = []

    for i in arr:
        temp = ''
        for j in range(len(i)):
            if j == 0:
                if i[j].isdigit() == False:
                    temp += i[j].upper()
                else:
                    temp += i[j]

            else:
                 temp += i[j].lower()
        else:
            arr1.append(temp)    


    return " ".join(arr1)
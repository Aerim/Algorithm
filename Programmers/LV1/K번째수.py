def solution(array, commands):
    answer=[]

    for command in commands:
        i=command[0]
        j=command[1]
        k=command[2]

        _array=array[i-1:j]
        _array.sort()
        temp=_array[k-1]
        answer.append(temp)
    return answer
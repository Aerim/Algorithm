def solution(sizes):

    temp_arr1 = []
    temp_arr2 = []

    for i in sizes:
        temp_arr1.append(max(i))
        temp_arr2.append(min(i))



    return max(temp_arr1) * max(temp_arr2)
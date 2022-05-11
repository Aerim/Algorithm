# 노래는 두개씩만 모음
def solution(genres, plays):
    answer = []

    dict = {}
    dict2 = {}

    for i, j in enumerate(zip(genres,plays)):

        if j[0] not in dict:
            dict[j[0]] = []
            dict[j[0]].append([i,j[1]])

            dict2[j[0]] = j[1]
        else:
            dict[j[0]].append([i,j[1]])

            dict2[j[0]] += j[1]

    arr = sorted(dict2.items(), key = lambda x : -x[1])

    for i,j in arr:
        arr1 = sorted(dict[i], key = lambda x : (-x[1],x[0]))

        if len(arr1) >= 2:
            for k in range(2):
                answer.append(arr1[k][0])

        elif len(arr1) < 2: 
            answer.append(arr1[0][0])  

    return answer
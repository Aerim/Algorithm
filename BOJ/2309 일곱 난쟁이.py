from itertools import permutations

arr = []

for i in range(9):
    arr.append(int(input()))
    
temp = list(permutations(arr,7))

res = []

for i in range(len(temp)):
    if sum(temp[i]) == 100:
        res.append(temp[i])
        break

res = sorted(res[0])

for i in range(len(res)):
    print(res[i])
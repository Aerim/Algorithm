from collections import defaultdict

def solution(friends, gifts):
    arr = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    dict = {}
    jisu = defaultdict(int)
    sunmul = defaultdict(int)
    
    for i in range(len(friends)):
        dict[friends[i]] = i
        jisu[friends[i]] = 0
        sunmul[friends[i]] = 0
    
    for i,j in enumerate(gifts):
        a = j.split(" ")[0]
        b = j.split(" ")[1]
        
        arr[dict[a]][dict[b]] += 1 
        jisu[a] += 1
        jisu[b] -= 1
  
    for i in range(len(friends)):
        for j in range(i+1):            
            if ((arr[i][j] > 0 or arr[j][i] > 0) and (arr[i][j] != arr[j][i])) :
                if arr[i][j] > arr[j][i]:
                    sunmul[friends[i]] += 1
                elif arr[i][j] < arr[j][i]:
                    sunmul[friends[j]] += 1
            elif(arr[i][j] == arr[j][i]):
                 if jisu[friends[i]] > jisu[friends[j]]:        
                    sunmul[friends[i]] += 1
                 elif jisu[friends[i]] < jisu[friends[j]]:  
                    sunmul[friends[j]] += 1
  
    return max(list(sunmul.values()))
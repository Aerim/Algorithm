arr = list(map(int,input().split()))

dict = {}

for i in arr:
    if i not in dict:
        dict[i] = 1
    
    else:
        dict[i] += 1   
        
arr1 = list(sorted(dict.items(), key = lambda x: x[0], reverse=True))
        
if len(dict) == 1:
    print(10000 + list(dict.keys())[0] * 1000)
     
elif len(dict) == 2:
    for k,v in dict.items():
        if v == 2:
            print(1000 + k * 100)
     
else:
    print(arr1[0][0]*100)
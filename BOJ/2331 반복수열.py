a, p = map(int,input().split())

prev = a
res = []
res.append(a)

while True:
    
    temp = 0
    prev = str(prev)
    
    for i in range(len(prev)):
        
        temp += int(prev[i]) ** p
        
    else:
        
        if temp in res:
            idx = res.index(temp)
            print(idx)
            break
            
        res.append(temp)
        prev = temp
            
    
    
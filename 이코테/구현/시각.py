num = int(input())

count = 0

for i in range(0,num+1):
    for j in range(0,60):
        for k in range(0,60):
            time = str(i) + str(j) + str(k)
            
            if time.find('3') != -1:
                count+=1

print(count)
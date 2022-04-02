i = input()

front=i[0:len(i)//2]
back=i[len(i)//2:]

sum_front=0
sum_back=0

for j in front:
    sum_front+=int(j)

for k in back:
    sum_back+=int(k)

if(sum_front == sum_back):
    print("LUCKY")

else: print("READY")
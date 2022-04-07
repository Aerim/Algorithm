""""
10  
1 0 1 1 1 0 0 1 1 0

"""

n = int(input())

arr = list(map(int,input().split()))
arr1 = [0 for i in range(n)]

flag = 0

for i in range(n):
   
   if arr[i] == 1:
       if flag == 1:
           arr1[i] = arr1[i-1] + 1
        
       else:
           arr1[i] = 1
           flag = 1
       
   else:
       flag = 0

print(sum(arr1))
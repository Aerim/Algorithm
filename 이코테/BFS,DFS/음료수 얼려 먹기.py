
n,m = list(map(int,input().split()))

arr = []
for i in range(0,n):
    arr.append(list(map(int,input())))


count = 0

def dfs(x,y):

    if x < 0 or y < 0 or x >= n or y >= m :
        return False

    if arr[x][y] == False:

        arr[x][y] = True
    
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True

for i in range(n):
    for j in range(m):

        if dfs(i,j) == True:
            count+=1
            
print(count)
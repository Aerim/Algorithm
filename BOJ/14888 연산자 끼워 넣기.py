# 숫자 순서 못바꿈 - 정렬 불가능
n = int(input())
arr = list(map(int,input().split()))
# + - * /
op = list(map(int,input().split()))
res = []

def dfs(plus,minus,div,mod,result,cnt):
    
    if cnt == n:
        res.append(result)
        return res
    
    if plus > 0:
        dfs(plus-1,minus,div,mod,result+arr[cnt],cnt+1)
    if minus > 0:
        dfs(plus,minus-1,div,mod,result-arr[cnt],cnt+1)
    if div > 0:
        dfs(plus,minus,div-1,mod,result*arr[cnt],cnt+1)
    # 나누기 주의
    if mod > 0:
        dfs(plus,minus,div,mod-1,int(result/arr[cnt]),cnt+1)

# arr1부터 더해야함
dfs(op[0],op[1],op[2],op[3],arr[0],1)

print(max(res))
print(min(res))
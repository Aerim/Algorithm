
# map 함수 : 한꺼번에 요소에 함수 적용

num = int(input())
arr=list(map(str,input().split()))

x,y = 1,1

type=['L','R','U','D']

# 이동 좌표값 매칭
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for _arr in arr:

    for i in range(len(type)):
        if _arr == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > num or ny > num:
        continue

    x,y = nx, ny

print(x,y)
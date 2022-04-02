n,m = list(map(int,input().split()))
nowx, nowy, dir = list(map(int,input().split()))

# map 정보저장
arr = []

for i in range(0,n):
    arr.append(list(map(int,input().split())))

# 북서남동
order = [0, 3, 2, 1]

# 캐릭터 이동 방향
change_dir = {'0': [-1,0], '3': [0,-1], '2': [1,0], '1' : [0,1]}

# 방문한 칸 저장 배열
visited = [[0] * m for _ in range(n)]
count = 1

# 방향 센 횟수 체크
_check = 0
  
while True:
    
    #  현재 칸 방문
    visited[nowx][nowy] = 1

    # 회전
    i = order.index(dir)

    if i < 3:
        dir = order[i+1]
    else:
        dir = order[0]

    # 방향에 대해 얼마나 이동해야하는가?
    temp = change_dir.get(str(dir))

    # 이동할 좌표
    nx = nowx + temp[0]
    ny = nowy + temp[1]

    # 방문하지 않은 칸이 존재 and 바다가 아님
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
    
        visited[nx][ny] = 1
        nowx = nx
        nowy = ny

        count += 1
        _check = 0
        
    # 왼쪽 칸 이미 방문함 or 바다
    # 방문하지 않은것은 넘어가기 때문에 방문한 칸이 있는 경우 
    # 방향 센 횟수 체크해야함
    else:
        _check += 1
    
    # 4방향 모두 바다일때도 해당이 된다 
    # else 문에서 체크했기 때문에
    if _check == 4:

        temp = change_dir.get(str(dir))
        
        nx = nowx - temp[0] 
        ny = nowy - temp[1]

        if arr[nx][ny] == 0:
            
            nowx= nx
            nowy = ny
        
        else : 
            break

        _check = 0

print(count)

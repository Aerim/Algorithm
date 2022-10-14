n = int(input())
student = []
arr = [[0] * n for _ in range(n)]
dict = {}
ans = 0

for i in range(n**2):
    student.append(list(map(int,input().split())))
    
dx = [-1,0,0,1]
dy = [0,1,-1,0]

for s in student:
    
    s_num = s[0]
    s_list = s[1:]
    
    temp = []
    dict[s_num] = s_list

    for i in range(n):
        for j in range(n):
            
            like = 0
            empty = 0
            # 비어 있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸 구하기
            if arr[i][j] == 0:
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in s_list:
                            like += 1
                            
                        if arr[nx][ny] == 0:
                            empty += 1
                
                
                temp.append([like,empty,i,j])
                
    # like,empty는 큰 순으로 행 열은 작은순으로
    temp.sort(key = lambda x : (-x[0],-x[1],x[2],x[3])) 
    
    x = temp[0][2]
    y = temp[0][3]
    
    arr[x][y] = s_num    

# 인접한 칸에 앉은 좋아하는 학생의 수 구해서 만족도 구하기
for i in range(n):
    for j in range(n):
        
        s_num = arr[i][j]
        s_list = dict[s_num]
        cnt = 0
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in s_list:
                    cnt += 1
                    
        if cnt == 1:
            ans += 1
        
        elif cnt == 2:
            ans += 10
            
        elif cnt == 3:
            ans += 100
            
        elif cnt == 4:
            ans += 1000
            
print(ans)
                    
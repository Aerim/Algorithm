def solution(board, h, w):
    
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    answer = 0
    
    for i in range(4):
        x = h + dx[i]
        y = w + dy[i]
        
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            continue
        
        if board[h][w] == board[x][y] :
            answer += 1
            
    return answer
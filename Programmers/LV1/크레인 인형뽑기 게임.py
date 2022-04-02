def solution(board, moves):
    answer = 0
    stack = []
    
    for i in range(len(moves)):    
        temp = moves[i]-1
        for j in range(len(board)):
            
            # 뽑으려는 자리에 인형이 존재하면
            if board[j][temp] != 0 :
                # 인형뽑고 stack에 push
                stack.append(board[j][temp])
                board[j][temp] = 0
                
                # stack에서 같은 인형이 2개 연속올때를 체크
                if len(stack) > 1 :
                    
                    len_stack = len(stack)-1
                    if stack[len_stack-1] == stack[len_stack]:
                        answer+=2
                        stack.pop()
                        stack.pop()
                break
            
  
    return answer
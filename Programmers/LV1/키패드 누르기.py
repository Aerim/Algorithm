def solution(numbers, hand):
    answer = ''
    # 초기값
    left_cur = 10
    right_cur = 12   
    
    for n in numbers:
        
        # 거리 계산을 위해 숫자로 바꾸기
        if n == 0 :
            n = 11
    
        # left일때 1,4,7
        if n == 1 or n == 4 or n == 7 :
            left_cur = n
            answer += 'L'
        # right일때 3,6,9
        elif n == 3 or n == 6 or n == 9 :
            right_cur = n
            answer += 'R'
        # 2,5,8,0 일 때
            # 거리계산
        else:
                
            temp_l = abs(n - left_cur) // 3 + abs(n - left_cur) % 3
            temp_r = abs(n - right_cur) // 3 + abs(n - right_cur) % 3
      
            print(left_cur, right_cur, temp_l,temp_r)
            if temp_l < temp_r :
                left_cur = n
                answer += 'L'
            elif temp_r < temp_l :
                right_cur = n
                answer += 'R'
            elif temp_r == temp_l :
                if hand == 'left':
                    left_cur = n
                    answer += 'L'
                else :
                    right_cur = n
                    answer += 'R'
                    
    return answer
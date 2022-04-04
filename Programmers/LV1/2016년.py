def solution(a, b):
    answer = ''
    
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']

    current_date = 0
    
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(a):
        current_date += month[i]
        
    current_date += b
    print(current_date)
    
    index = current_date % 7
    
    answer = day[index]
        
    return answer
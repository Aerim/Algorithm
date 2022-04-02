def solution(numbers):
    answer = 0
    
    numbers = sorted(numbers)
   
    num_array = [i for i in range(0,10)]
    
    for i in range(len(num_array)):
        if num_array[i] not in numbers:
            answer += num_array[i]
            
    return answer
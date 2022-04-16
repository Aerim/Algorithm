def solution(record):
    answer = []
    temp = []
    
    dict = {}
    
    for i in record:
        
        if i.split(' ')[0] != 'Leave':
            status = i.split(' ')[0]
            id =  i.split(' ')[1]
            name = i.split(' ')[2]
            
            dict[id] = name
                
            if status == 'Enter':
                temp.append([status,id])
    
        else:
            status = i.split(' ')[0]
            id =  i.split(' ')[1]
            
            name = dict[id]
            
            temp.append([status,id])
    
    for i,j in temp:
        if i == 'Enter':
            answer.append(dict[j]+'님이 들어왔습니다.')
        elif i == 'Leave':
            answer.append(dict[j]+'님이 나갔습니다.')
        
    return answer
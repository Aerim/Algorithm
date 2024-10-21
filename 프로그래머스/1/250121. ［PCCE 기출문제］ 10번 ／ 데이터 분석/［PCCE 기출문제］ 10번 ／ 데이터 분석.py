def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    dict = {"code":0 , "date":1, "maximum":2, "remain":3}
    
    data.sort(key = lambda x: x[dict[ext]])
    
    for i in range(len(data)):
        if data[-1][dict[ext]] < val_ext:
            break
        else:
            data.pop()
   
    return sorted(data, key = lambda x : x[dict[sort_by]])
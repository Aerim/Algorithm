def solution(id_list, report, k):
    answer = []
    
    dict = {}
    dict2 = {}
    dict3 = {}
    cancle = []
    
    for i in id_list:
        dict2[i] = 0
        dict3[i] = 0
        
    for i in report:
        reporter = i.split()[0]
        reported = i.split()[1]
        
        # 첫 신고
        if reporter not in dict:
            dict[reporter] = [reported]
            dict2[reported] += 1
        else:
            if reported not in dict[reporter] :
                dict[reporter].append(reported)
                dict2[reported] += 1
    else :
        for key,value in dict2.items():
            if int(value) >= int(k):
                cancle.append(key)
    
    for key,value in dict.items():
        for v in value:
            if v in cancle:
                dict3[key] += 1
            
 
    return list(dict3.values())
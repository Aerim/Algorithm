def solution(lottos, win_nums):
    answer = []
    
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    
    # 일치한 개수
    count = 0
    
    zero_count = lottos.count(0)
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1
            
    
    max_lottos = count + zero_count
    min_lottos = count
            
    max_ranking = 7 - max_lottos
    min_ranking = 7 - min_lottos
    
    if max_ranking == 7:
        max_ranking = 6
        
    if min_ranking == 7:
        min_ranking = 6
    
    return [max_ranking,min_ranking]
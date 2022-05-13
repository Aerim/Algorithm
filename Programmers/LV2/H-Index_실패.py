def solution(citations):
   
    citations = sorted(citations)
    max_index  = len(citations)-1
    
    for i in range(0, (citations[max_index])//2+1) :
        
        high, low = 0, 0
        
        for j in range(0, max_index+1):
            # 인용횟수가 i번이상
            if citations[j] >= i:
                high += 1
            if citations[j] <= i:
                low += 1
            
            # low = max_index-high+1
        print(i,high,low)
        
        # 같은 값을 가지는 인용횟수가 등장하면?
        if high == i:
            print('equal')
            return i
       
      
    else: 
        print('not equal')
        return citations[max_index//2]
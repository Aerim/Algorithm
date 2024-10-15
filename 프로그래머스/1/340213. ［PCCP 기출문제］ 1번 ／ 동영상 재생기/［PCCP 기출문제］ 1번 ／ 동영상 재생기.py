def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    v_len = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
   
    c_pos = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
     
    o_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
 
    o_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
  
    for c in commands:
        if o_start <= c_pos <= o_end :
            c_pos = o_end
        
        if c == "next":
            c_pos += 10
            
            if v_len - c_pos < 10:
                c_pos = v_len
            elif c_pos > v_len:
                c_pos = v_len
                
        elif c == "prev":
            c_pos -= 10
            
            if c_pos < 10 :
                c_pos = 0
            elif c_pos < 0:
                c_pos = 0
    
    if o_start <= c_pos <= o_end :
            c_pos = o_end
            
    answer = str(c_pos // 60).zfill(2) + ":" + str(c_pos % 60).zfill(2)         
    return answer
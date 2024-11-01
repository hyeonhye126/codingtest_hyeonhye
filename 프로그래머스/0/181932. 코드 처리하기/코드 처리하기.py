def solution(code):
    mode = 0
    ret = ''
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == '1':
                mode = 1
            else: 
                if idx % 2 == 0:
                    ret += (code[idx])
        else: # mode == 1
            if code[idx] == '1':
                mode = 0
            else:
                if idx % 2 != 0:
                    ret += (code[idx])   
                    
    if not ret:
        ret = "EMPTY"
        
    return ret
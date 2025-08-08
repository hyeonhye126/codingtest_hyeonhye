def solution(my_string, m, c):    
    chunks = []
    for i in range(0, len(my_string), m):
        chunks.append(my_string[i:i+m])
    
    answer = [ch[c-1] for ch in chunks]
    
    answer = ''.join(answer)
    
    return answer
def solution(name, yearning, photo):
    answer = []
    
    name_dic = {name: score for name, score in zip(name, yearning)}
    
    for pho in photo:
        tmp = 0
        for p in pho:
            tmp += name_dic.get(p, 0)
        answer.append(tmp)
    
    return answer
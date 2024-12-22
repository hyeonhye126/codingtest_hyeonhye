def solution(spell, dic):
    answer = 2 
    for d in dic:
        cnt = 0
        for s in spell:
            if s in d:
                cnt += 1
        if cnt == len(spell):
            answer = 1
    return answer
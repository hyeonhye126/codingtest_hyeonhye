from collections import Counter

def solution(before, after):
    if Counter(before) == Counter(after):
        flag = 1
    else:
        flag = 0
    
    return flag
from collections import Counter

def solution(strArr):    
    counts = Counter(len(s) for s in strArr)
    return max(counts.values())
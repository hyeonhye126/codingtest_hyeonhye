from itertools import permutations

def solution(babbling):
    words = ['aya','ye','woo','ma']
    possible = set()
    
    for i in range(1, 5):
        for p in permutations(words, i):
            possible.add(''.join(p))
        
    result = sum(1 for b in babbling if b in possible)
    return result
def solution(myString, pat):
    idx = 0
    
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            idx = i + len(pat)
            
    return myString[:idx]
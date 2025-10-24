def solution(arr):
    stk = []
    
    for a in arr:
        if stk and stk[-1] == a:
            stk.pop()
        else:
            stk.append(a)    
    
    return stk if stk else [-1]
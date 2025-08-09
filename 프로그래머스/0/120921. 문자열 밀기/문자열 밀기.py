def solution(A, B):
    flag = 0
    
    if A == B:
        return 0
    
    for i in range(len(A)):
        if B == (A[-1] + A[:-1]):
            flag = 1
            tmp = i + 1
            break;
        else:
            A = A[-1] + A[:-1]
    
    if flag:
        return tmp
    else:
        return -1 
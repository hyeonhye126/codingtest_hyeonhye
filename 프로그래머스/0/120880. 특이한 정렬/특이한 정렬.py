def solution(numlist, n):
    for i in range(len(numlist)):
        for j in range(i, len(numlist)):
            x = abs(numlist[i] - n)
            y = abs(numlist[j] - n)
            
            if x >= y:
                if x == y:
                    if numlist[i] < numlist[j]:
                        tmp = numlist[i]
                        numlist[i] = numlist[j]
                        numlist[j] = tmp
                else:
                    tmp = numlist[i]
                    numlist[i] = numlist[j]
                    numlist[j] = tmp
    return numlist
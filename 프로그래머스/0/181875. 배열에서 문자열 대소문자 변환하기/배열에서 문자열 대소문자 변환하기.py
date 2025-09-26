def solution(strArr):
    strArr[0] = strArr[0].lower()
    for i in range(1, len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    return strArr
def solution(myString, pat):
    trans = str.maketrans({"A":"B", "B":"A"})
    swapped = myString.translate(trans)
    
    return 1 if pat in swapped else 0
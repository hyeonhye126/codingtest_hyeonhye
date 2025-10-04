def solution(rny_string):
    str = list(rny_string)
    for i in range(len(rny_string)):
        if str[i] == "m":
            str[i] = "rn"
    return ''.join(str)
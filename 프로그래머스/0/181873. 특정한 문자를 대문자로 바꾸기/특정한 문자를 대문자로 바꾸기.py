def solution(my_string, alp):
    my_string = list(my_string)
    for m in my_string:
        if m == alp:
            for i in range(len(my_string)):
                if my_string[i] == alp:
                    my_string[i] = my_string[i].upper()
            break
    return ''.join(my_string)
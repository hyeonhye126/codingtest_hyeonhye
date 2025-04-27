def solution(my_strings, parts):
    result = ''
    for string, (start, end) in zip(my_strings, parts):
        result += string[start:end+1]
    return result
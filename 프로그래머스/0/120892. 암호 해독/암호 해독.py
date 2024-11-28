def solution(cipher, code):
    # i = code - 1
    # answer = ''
    # while i < len(cipher):
    #     answer += cipher[i]
    #     i += code
    return cipher[code-1::code]
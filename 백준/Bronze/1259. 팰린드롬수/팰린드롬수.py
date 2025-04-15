while (True):
    input_num = input()

    if input_num == "0": break

    if input_num == input_num[::-1]:
        answer = "yes"
    else:
        answer = "no"
        
    print(answer)

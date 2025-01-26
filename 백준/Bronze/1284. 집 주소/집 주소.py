while(1):
    user_input = int(input())
    if user_input == 0: 
        break

    result = 0
    num_list = list(map(int, str(user_input)))
    for n in num_list:
        if n == 0:
            result += 4
        elif n == 1:
            result += 2
        else:
            result += 3
    result += (len(num_list) - 1) + 2
    print(result)
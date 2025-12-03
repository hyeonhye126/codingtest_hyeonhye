N = int(input())

if N == 1:
    print(1)
else:
    step = 1
    max_num = 1
    add = 6

    while N > max_num:
        max_num += add
        add += 6
        step += 1

    print(step)
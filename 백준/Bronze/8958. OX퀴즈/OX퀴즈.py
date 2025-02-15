n = int(input())

for i in range (n):
    score = input()
    result = 0
    a = 1
    for i in score:
        if (i == 'O'):
            result += a
            a += 1
        else:
            a = 1
    print(result)

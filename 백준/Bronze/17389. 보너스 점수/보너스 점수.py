N = int(input())
string = input()

bonus = 0
result = 0

for i in range(N):
    if string[i] == 'X':
        bonus = 0
    elif string[i] == 'O':
        result = result + bonus + (i + 1)
        bonus += 1

print(result)

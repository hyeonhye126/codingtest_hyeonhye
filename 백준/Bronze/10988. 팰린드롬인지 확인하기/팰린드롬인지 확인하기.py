str = input()

strlen = len(str)
a = 1

for i in range ((int)(strlen/2)):
    if (str[i] == str[strlen - i - 1]):
        continue
    else:
        a = 0
        break

if (a == 1): print(1)
else: print(0)

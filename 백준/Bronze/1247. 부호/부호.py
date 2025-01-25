import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    flag = sum(int(input()) for _ in range(N))
    if flag == 0:
        print(0)
    elif flag < 0:
        print('-')
    else:
        print('+')
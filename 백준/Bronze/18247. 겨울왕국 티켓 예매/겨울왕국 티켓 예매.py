test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())

    if N < 12 or M < 4:
        print(-1)
    else:
        print(M * 11 + 4)
        
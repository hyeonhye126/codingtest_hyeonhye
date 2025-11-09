cnt = 1

while True:
    N = int(input())
    if N == 0: break

    list = []
    for i in range(N):
        name = input()
        list.append([i+1, name])

    check = []
    for i in range((2*N - 1)):
        n, x = input().split()
        n = int(n)
        if n not in check:
            check.append(n)
        elif n in check:
            idx = check.index(n)
            check.pop(idx)

    id = check[0]
    print(cnt, list[id - 1][1])
    cnt += 1
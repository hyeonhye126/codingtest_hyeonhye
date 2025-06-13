N, K = map(int, input().split())

count = 0
flag = 0

for i in range (1, N + 1):
    if N % i == 0:
        count += 1
        if count == K:
            print(i)
            flag = 1
            break
    i += 1

if not flag:
    print(0)
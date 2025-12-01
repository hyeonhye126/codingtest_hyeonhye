N = int(input())

for candidate in range(max(1, N - 54), N + 1):
    if candidate + sum(map(int, str(candidate))) == N:
        print(candidate)
        break
else:
    print(0)
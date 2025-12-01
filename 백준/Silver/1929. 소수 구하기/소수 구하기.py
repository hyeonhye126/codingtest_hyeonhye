import math

M, N = map(int, input().split())

for i in range(M, N + 1):
    if i == 1:
        continue  # 1은 소수 아님

    is_Prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_Prime = False
            break
    if is_Prime:
        print(i)
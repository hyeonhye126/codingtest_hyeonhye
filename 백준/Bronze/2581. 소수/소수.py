M = int(input())
N = int(input())

answer = []
for i in range(M, N + 1):
    if i == 1:
        continue
        
    is_Prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_Prime = False
    if is_Prime:
        answer.append(i)

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)
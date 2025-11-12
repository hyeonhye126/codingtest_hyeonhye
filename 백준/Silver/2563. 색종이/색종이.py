n = int(input())
paper = [[0] * 100 for i in range(100)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            paper[i][j] = 1

area = 0

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

print(area)
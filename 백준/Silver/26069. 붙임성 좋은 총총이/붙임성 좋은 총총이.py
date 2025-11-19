N = int(input())

name = {"ChongChong"}
cnt = 0

for _ in range(N):
    a, b = input().split()

    if a in name or b in name:
        name.add(a)
        name.add(b)

print(len(name))
N = int(input())

name = set()
cnt = 0

for _ in range(N):
    s = input().strip()
    if s == "ENTER":
        name.clear()
    if s != "ENTER" and s not in name:
        name.add(s)
        cnt += 1

print(cnt)
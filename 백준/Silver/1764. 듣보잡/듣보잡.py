M, N = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(M):
    set1.add(input())
for _ in range(N):
    set2.add(input())

answer = set1 & set2

print(len(answer))
for a in sorted(answer):
    print(a)
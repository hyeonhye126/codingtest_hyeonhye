import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)
subs = set()

for i in range(n):
    for j in range(i+1, n+1):
        subs.add(S[i:j])

print(len(subs))
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

answer = []

for ch in check:
    if ch in cards:
        answer.append(1)
    else:
        answer.append(0)

print(' '.join(map(str, answer)))
total = int(input())
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    total -= a * b
print("Yes" if total == 0 else "No")
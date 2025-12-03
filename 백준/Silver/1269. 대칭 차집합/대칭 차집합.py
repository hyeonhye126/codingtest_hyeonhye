M, N = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

answer = len(A - B) + len(B - A)
print(answer)
A, B, N = map(int, input().split())

num = A * (10 ** N) // B
digit = num % 10

print(digit)
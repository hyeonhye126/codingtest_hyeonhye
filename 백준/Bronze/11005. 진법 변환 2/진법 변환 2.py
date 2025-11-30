N, B = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if N == 0:
    print(0)
else:
    result = ""
    while N > 0:
        result += digits[N % B]
        N //= B

print(result[::-1])
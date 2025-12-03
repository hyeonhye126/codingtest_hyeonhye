A, B, V = map(int, input().split())

if V <= A:
    print(1)
else:
    # (V - A)를 (A - B)로 나눈 올림한 값에 1을 더함
    days = (V - A + (A - B) - 1) // (A - B) + 1
    print(days)
X = int(input())

n = 1
total = 1  # 1 + 2 + ... + n

# 몇 번째 대각선(n)에 X가 속하는지 찾기
while total < X:
    n += 1
    total += n

# 이전 대각선까지의 총 개수 = total - n
offset = X - (total - n)  # 해당 대각선 안에서의 위치 (1-based)

if n % 2 == 0:
    # 짝수 대각선: 아래->위 (offset / (n-offset+1))
    numerator = offset
    denominator = n - offset + 1
else:
    # 홀수 대각선: 위->아래 ((n-offset+1) / offset)
    numerator = n - offset + 1
    denominator = offset

print(f"{numerator}/{denominator}")
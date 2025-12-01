import math

a, b = map(int, input().split())
c, d = map(int, input().split())

g = math.gcd(b, d)
den = b // g * d # 최소 공배수
num = a * (den // b) + c * (den // d)

g2 = math.gcd(num, den)
num //= g2
den //= g2

print(num, den)
import math

A, B = map(int, input().split())

g = math.gcd(A, B)
lcm = A // g * B
print(lcm)
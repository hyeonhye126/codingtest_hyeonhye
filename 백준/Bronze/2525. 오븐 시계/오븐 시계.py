h, m = map(int, input().split())
cook_m = int(input())

h += cook_m // 60
m += cook_m % 60

if m >= 60:
    h += 1
    m -= 60

if h >= 24:
    h -= 24

print(h, m)
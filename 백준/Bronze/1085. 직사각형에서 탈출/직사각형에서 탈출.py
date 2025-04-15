x, y, w, h = map(int, input().split())

num = []

num.append(w - x)
num.append(h - y)
num.append(x - 0)
num.append(y - 0)

print(min(num))

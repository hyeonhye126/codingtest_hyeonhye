x, y = map(int, input().split())
num = list(map(int, input().split()))
ans = []

for i in range (5):
    ans.append(num[i] - x*y)

for i in range (5):
    print(ans[i], "", end='')

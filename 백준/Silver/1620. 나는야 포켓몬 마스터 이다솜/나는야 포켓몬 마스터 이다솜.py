N, M = map(int, input().split())

dic = {}
for i in range(1, N + 1):
    name = input()
    dic[i] = name
    dic[name] = i

for j in range(M):
    x = input()
    if x.isdigit():
        print(dic[int(x)])
    else:
        print(dic[x])
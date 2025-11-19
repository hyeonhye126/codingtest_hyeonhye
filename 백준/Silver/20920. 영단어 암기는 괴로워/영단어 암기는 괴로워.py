N, M = map(int, input().split())

dic = {}

for _ in range(N):
    s = input().strip()

    if len(s) >= M:
        dic[s] = dic.get(s, 0) + 1

sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, freq in sorted_dic:
    print(word)
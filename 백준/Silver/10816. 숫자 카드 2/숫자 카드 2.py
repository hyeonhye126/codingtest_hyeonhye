N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

dic = {}
for x in n_list:
    dic[x] = dic.get(x, 0) + 1

ans = []
for x in m_list:
    ans.append(str(dic.get(x, 0)))

print(' '.join(ans))
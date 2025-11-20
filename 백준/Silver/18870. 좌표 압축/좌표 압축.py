N = int(input())
numlist = list(map(int, input().split()))

sorted_list = sorted(set(numlist))

rank = {value: idx for idx, value in enumerate(sorted_list)}

print(*[rank[x] for x in numlist])

# rank = {}
# idx = 0
# for value in sorted_list:
#     rank[value] = idx
#     idx += 1

# result = []
# for x in numlist:
#     result.append(rank[x])

# print(*result)
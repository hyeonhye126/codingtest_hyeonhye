from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, len(nums) + 1):
    for comb in combinations(nums, i):
        if sum(comb) == S:
            cnt += 1

print(cnt)
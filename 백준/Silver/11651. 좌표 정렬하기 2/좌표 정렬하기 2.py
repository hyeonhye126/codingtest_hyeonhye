N = int(input())

nums = []

for _ in range(N):
    x, y = map(int, input().split())
    nums.append([x, y])

nums = sorted(nums, key=lambda x: (x[1], x[0]))

for i in range(N):
    print(nums[i][0], nums[i][1])
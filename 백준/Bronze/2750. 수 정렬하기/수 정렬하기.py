N = int(input())

nums = []
for i in range (N):
    x = int(input())
    nums.append(x)

nums.sort()

for i in range (N):
    print(nums[i])

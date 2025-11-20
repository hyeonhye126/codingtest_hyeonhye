from collections import Counter

N = int(input())
nums = [int(input()) for _ in range(N)]

# 1) 산술평균: "소수점 첫째 자리에서 반올림"
s = sum(nums)
avg = s / N
if avg >= 0:
    one = int(avg + 0.5)
else:
    one = int(avg - 0.5)

# 2) 중앙값 (정렬 후 가운데)
nums.sort()
two = nums[N // 2]

# 3) 최빈값: 여러 개면 '두 번째로 작은 값' 출력
counter = Counter(nums) 
max_freq = max(counter.values())
modes = [num for num, freq in counter.items() if freq == max_freq]
modes.sort()
three = (modes[0] if len(modes) == 1 else modes[1])

# 4) 범위
four = nums[-1] - nums[0]

result = [one, two, three, four]
for r in result:
    print(r)
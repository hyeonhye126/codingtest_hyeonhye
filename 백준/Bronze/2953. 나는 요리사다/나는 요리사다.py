arr = []

for i in range (5):
    row = list(map(int, input().split()))
    arr.append(row)

max_sum = -1
max_index = -1

for i in range(5):
    row_sum = sum(arr[i])
    if row_sum > max_sum:
        max_sum = row_sum
        max_index = i + 1

print(max_index, max_sum)
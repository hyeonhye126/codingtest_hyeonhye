N = int(input())
A = list(map(int, input().split()))

left = A[0]
right = A[-1]

k = N - 2

while k > 0:
    if k == 1:
        left -= 1
        right -= 1
    else:
        if left > right:
            left -= 1
        else:
            right -= 1
    k -= 1

print(max(left, right))
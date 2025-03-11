n = int(input())

num = list(map(int, input().split()))

ans = 0
for i in range (n):
    cnt = 0
    a = num[i]
    
    for j in range (1,a+1):
        if ((int)(a%j) == 0):
            cnt += 1

    if (cnt == 2):
        ans += 1

print(ans)

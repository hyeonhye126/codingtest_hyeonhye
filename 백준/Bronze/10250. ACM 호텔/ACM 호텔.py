num = int(input())

for i in range (num):
    H, W, N = map(int, input().split())

    a = int(N % H)
    if a == 0:
        a = H
        b = int(N / H)
    else:
        b = int(N / H) + 1
    
    print(int(a*100 + b))

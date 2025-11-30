T = int(input())

for _ in range(T):
    N = int(input())

    res = [0,0,0,0]
    
    res[0] = N // 25
    res[1] = N % 25 // 10
    res[2] = N % 25 % 10 // 5
    res[3] = N % 25 % 10 % 5

    print(res[0], res[1], res[2], res[3])
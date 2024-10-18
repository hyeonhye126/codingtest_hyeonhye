while(1):
    n = input()
    if n == '0':
        break
    
    print(n, end=' ') 
    while (len(n) > 1):
        res = 1
        for c in n:
            res *= int(c)
        print(res, end = ' ')
        n = str(res)    
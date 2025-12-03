import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n + 1, 2 * n + 1):
        is_prime = True
        
        if i < 2:
            is_prime = False
        else:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1

    print(count)
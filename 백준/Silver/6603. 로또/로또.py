from itertools import combinations

first = True

while True:
    x = list(map(int, input().split()))
    if x[0] == 0:
        break
    
    k = x[0]
    num_list = x[1:]

    if not first:
        print()
    first = False

    for comb in combinations(num_list, 6):
        print(*comb)
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(int(input()) for _ in range(N))
num_list.sort()

for num in num_list:
    print(num)
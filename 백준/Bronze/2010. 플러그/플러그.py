import sys
input = sys.stdin.readline

N = int(input())

plugs = 0
for _ in range(N):
    plugs += int(input())
    
print(plugs - (N - 1))
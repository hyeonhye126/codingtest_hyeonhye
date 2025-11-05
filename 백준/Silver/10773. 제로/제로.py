K = int(input())
stack = []

for i in range(K):
    x = int(input())
    
    if x == 0:
        stack.pop()
    else:
        stack.append(x)

print(sum(stack))
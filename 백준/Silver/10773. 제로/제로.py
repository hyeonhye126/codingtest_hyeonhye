K = int(input())
stack = []

for i in range(K):
    x = int(input())
    
    if x == 0:
        if stack:
            stack.pop()
        else:
            continue
    else:
        stack.append(x)

print(sum(stack))
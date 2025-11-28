s = input().strip()
bomb = input()

L = len(bomb)
bomb_list = list(bomb)

stack = []
for ch in s:
    stack.append(ch)
    if len(stack) >= L and stack[-L:] == bomb_list:
        del stack[-L:]

result = "".join(stack)
print(result if result else "FRULA")
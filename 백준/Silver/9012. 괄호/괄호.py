N = int(input())

for _ in range(N):
    s = input().strip()
    stack = []

    for ch in s:
        if ch == "(":
            stack.append(ch)
        else: # ch == ")"
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(ch)

    print("YES" if not stack else "NO")
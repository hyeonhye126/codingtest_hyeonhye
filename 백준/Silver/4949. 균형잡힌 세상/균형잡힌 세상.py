while True:
    x = input()
    if x[0] == ".":
        break

    s = [ch for ch in x if ch in "[]()"]

    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == "[":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        else: # c == "]"
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)

    print("yes" if not stack else "no")
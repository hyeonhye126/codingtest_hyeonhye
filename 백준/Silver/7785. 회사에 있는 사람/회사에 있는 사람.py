N = int(input())

current = set()

for i in range(N):
    name, action = input().split()

    if action == "enter":
        current.add(name)
    elif action == "leave":
        current.remove(name)

for name in sorted(current, reverse=True):
    print(name)
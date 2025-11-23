lines = [input().rstrip() for _ in range(5)]

result = ""

for col in range(15):
    for row in range(5):
        if col < len(lines[row]):
            result += lines[row][col]

print(result)
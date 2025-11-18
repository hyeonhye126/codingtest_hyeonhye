maxnum = -1
numlist = []
a = b = 0


for i in range(9):
    row = list(map(int, input().split()))
    numlist.append(row)

for i in range(9):
    for j in range(9):
        if maxnum < numlist[i][j]:
            maxnum = numlist[i][j]
            a, b = i, j

print(maxnum)
print(a+1, b+1)
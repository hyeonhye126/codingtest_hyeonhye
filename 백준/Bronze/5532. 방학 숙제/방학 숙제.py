L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

a = A//C
if (int(A%C) != 0): a +=1

b = B//D
if (int(A%C) != 0): b +=1

c = max(a,b)

print(L - c)

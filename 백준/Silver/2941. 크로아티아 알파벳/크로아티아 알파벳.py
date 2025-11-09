alphabet = ["c=", "c-", "dz=","d-","lj","nj","s=","z="]

s = input().strip()

cnt = 0
for a in alphabet:
    s = s.replace(a, "*")
   
print(len(s))
N = int(input())
call = list(map(int, input().split()))

youngsik = 0
minsik = 0

for t in call:
    youngsik += 10 * (t // 30 + 1)
    minsik += 15 * (t // 60 + 1)

if youngsik > minsik:
    print("M", minsik)
elif minsik > youngsik:
    print("Y", youngsik)
else:
    print("Y M", youngsik)
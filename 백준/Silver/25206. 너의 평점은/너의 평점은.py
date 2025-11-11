subject = [[0] * 3 for i in range(20)]

score = {"A+": 4.5, "A0":4.0, "B+":3.5, "B0":3.0,
         "C+": 2.5, "C0":2.0, "D+":1.5, "D0":1.0,
         "F":0.0}

sum_, hakjum = 0, 0

for i in range(20):
    subject[0], subject[1], subject[2] = input().split()
    subject[1] = float(subject[1])
    if subject[2] == "P":
        continue
    sum_ += (int(subject[1]) * score[subject[2]])
    hakjum += int(subject[1])

print("%.6f" %(sum_/hakjum))
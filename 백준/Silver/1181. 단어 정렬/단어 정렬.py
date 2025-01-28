N = int(input())
num_list = []

for i in range(N):
    num_list.append(input())

sorted_list = sorted(set(num_list), key=lambda x: (len(x), x))

for i in range(len(sorted_list)):
    print(sorted_list[i])
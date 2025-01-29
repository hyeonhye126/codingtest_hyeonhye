num_list = list(int(input()) for _ in range(5))

print(int(sum(num_list) / 5)) # 평균
print(sorted(num_list)[2]) # 중앙값 
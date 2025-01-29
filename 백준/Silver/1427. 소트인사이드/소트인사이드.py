n_list = sorted(list(map(int, str(int(input())))), reverse=True)
result = int(''.join(map(str, n_list)))
print(result)
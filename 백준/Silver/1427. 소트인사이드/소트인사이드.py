n_list = sorted(list(map(int, str(int(input())))), reverse=True)
result = ''.join(map(str, n_list))
print(int(result))
str = input()

new_str = []

for ch in str:
    if ch.islower():
        new_str.append(ch.upper())
    else:
        new_str.append(ch.lower())

result = ''.join(new_str) # 리스트를 다시 문자열로 변환
print(result)
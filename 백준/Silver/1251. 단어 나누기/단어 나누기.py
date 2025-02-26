def find_smallest_reversed_word(word):
    n = len(word)
    min_word = "z" * (n + 1)  # 비교를 위한 초기값 (사전순으로 가장 뒤에 있는 단어)
    
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            part1 = word[:i][::-1]
            part2 = word[i:j][::-1]
            part3 = word[j:][::-1]
            new_word = part1 + part2 + part3
            
            if new_word < min_word:
                min_word = new_word
    
    return min_word

# 입력 받기
word = input().strip()
print(find_smallest_reversed_word(word))
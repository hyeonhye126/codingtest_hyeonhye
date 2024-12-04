from collections import Counter

def solution(s):
    # 각 문자의 등장 횟수를 세는 딕셔너리 생성
    char_count = Counter(s)
    
    # 등장 횟수가 1인 문자 필터링
    unique_chars = [char for char in char_count if char_count[char] == 1]
    
    # 사전 순으로 정렬
    unique_chars.sort()
    
    # 결과 문자열 반환
    return ''.join(unique_chars)

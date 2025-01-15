def solution(n):
    answer = n
    for i in range(1, n + 1):
        # 3의 배수이거나 3이 포함된 수만큼 답을 증가
        if i % 3 == 0 or '3' in str(i):
            answer += 1
            # 증가된 수가 3의 배수이거나 3이 포함된 경우 추가로 증가
            while answer % 3 == 0 or '3' in str(answer):
                answer += 1
    return answer
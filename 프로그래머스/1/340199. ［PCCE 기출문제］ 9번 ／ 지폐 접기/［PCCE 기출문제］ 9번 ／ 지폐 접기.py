def solution(wallet, bill):
    # 정렬해서 작은값/큰값을 대응시킴
    w = sorted(wallet)
    b = sorted(bill)
    
    answer = 0
    # bill이 wallet에 들어갈 때까지 반복
    while b[0] > w[0] or b[1] > w[1]:
        # 긴 쪽을 반으로 접음 (같으면 b[1]을 접어도 됨)
        if b[1] >= b[0]:
            b[1] = b[1] // 2
        else:
            b[0] = b[0] // 2
        answer += 1
        b.sort()
        
    return answer

def solution(rank, attendance):
    # 학생 번호와 등수를 묶고, 참석 가능한 학생만 필터링
    candidates = [(i, r) for i, (r, attend) in enumerate(zip(rank, attendance)) if attend]
    
    # 등수 기준으로 오름차순 정렬
    candidates.sort(key=lambda x: x[1])
    
    # 상위 3명의 학생 번호 추출
    a, b, c = candidates[0][0], candidates[1][0], candidates[2][0]
    
    # 수식 계산
    return 10000 * a + 100 * b + c
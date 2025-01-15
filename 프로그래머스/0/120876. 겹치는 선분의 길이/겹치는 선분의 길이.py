def solution(lines):
    # 전체 범위를 나타내는 배열 초기화 (-100에서 100까지)
    line_map = [0] * 201 # 인덱스 0 ~ 200 (실제 범위는 -100 ~ 100)
    
    for line in lines:
        # 좌료를 양수로 변환 (-100 -> 0, 0 -> 100, 100 -> 200)
        start = line[0] + 100
        end = line[1] + 100
        
        for i in range(start, end):
            line_map[i] += 1 # 각 선분마다 해당하는 부분에 1을 더함
    
    # 2 이상인 부분(겹치는 부분)의 개수를 셈
    return sum(1 for x in line_map if x >= 2)
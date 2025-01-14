def solution(polynomial):
    # 다항식을 공백 기준으로 분리
    terms = polynomial.split(" + ")
    
    # 계수 초기화
    x_coeff = 0  # x 항의 계수
    constant = 0  # 상수항
    
    # 각 항을 처리
    for term in terms:
        if 'x' in term:
            # 'x'가 포함된 경우
            if term == 'x':  # 계수가 생략된 경우 (계수 1)
                x_coeff += 1
            else:
                x_coeff += int(term.replace('x', ''))
        else:
            # 상수항인 경우
            constant += int(term)
    
    # 결과 문자열 조합
    result = []
    if x_coeff > 0:
        result.append(f"{x_coeff}x" if x_coeff > 1 else "x")  # 계수 1은 생략
    if constant > 0:
        result.append(str(constant))
    
    return " + ".join(result)

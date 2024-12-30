def solution(sides):
    """
    삼각형을 완성하기 위해 필요한 세 번째 변의 가능한 경우의 수를 계산합니다.

    :param sides: 두 변의 길이가 담긴 배열
    :return: 가능한 세 번째 변의 정수 개수
    """
    # 두 변을 정렬하여 작은 변(a)과 큰 변(b)을 구함
    sides.sort()
    a, b = sides

    # 세 번째 변이 가장 긴 변이 아닌 경우
    case_1 = (a + b - 1) - b  # 가능한 최소부터 최대까지의 범위

    # 세 번째 변이 가장 긴 변인 경우
    case_2 = (a + b) - (b + 1) + 1  # 가능한 최소부터 최대까지의 범위

    return case_1 + case_2
def solution(array, n):
    # array를 정렬합니다.
    array.sort()
    # array의 요소를 n과의 차이를 기준으로 정렬하고 가장 작은 차이를 가진 요소를 반환합니다.
    return min(array, key=lambda x: (abs(x - n), x))
def solution(number):
    num = sum(map(int, number.split()))
    answer = num % 9
    return answer
def solution(numbers):
    max_1 = max(numbers)
    numbers.pop(numbers.index(max_1))
    max_2 = max(numbers)
    return max_1 * max_2
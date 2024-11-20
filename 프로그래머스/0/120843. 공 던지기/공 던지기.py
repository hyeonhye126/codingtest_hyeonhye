def solution(numbers, k):
    return numbers[(2 * k - 2) % len(numbers)]
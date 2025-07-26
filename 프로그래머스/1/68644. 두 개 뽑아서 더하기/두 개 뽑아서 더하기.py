def solution(numbers):
    n_sum = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            n_sum.append(numbers[i] + numbers[j])
    answer = sorted(list(set(n_sum)))
    return answer
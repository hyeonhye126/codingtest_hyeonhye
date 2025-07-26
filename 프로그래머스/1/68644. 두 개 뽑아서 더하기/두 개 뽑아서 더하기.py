def solution(numbers):
    sum = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                sum.append(numbers[i] + numbers[j])
    sum = sorted(list(set(sum)))
    answer = sum
    return answer
def solution(arr, k):
    answer = []
    seen = set()
    
    for a in arr:
        if a in seen:
            continue
        seen.add(a)
        answer.append(a)
        if len(answer) == k:
            break

    answer += [-1] * (k - len(answer))
            
    return answer
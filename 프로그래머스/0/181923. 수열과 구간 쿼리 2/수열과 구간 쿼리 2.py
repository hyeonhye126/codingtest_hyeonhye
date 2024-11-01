def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        tmp = []
        for i in range(s, e + 1):
            if arr[i] > k:
                tmp.append(arr[i])
    
        if not tmp:
            answer.append(-1)
        else:
            result = min(tmp)
            answer.append(result)
                
    return answer
def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        min_ = 1000000
        for i in range(s, e + 1):
            if arr[i] > k:
                if min_ > arr[i]:
                    min_ = arr[i]
    
        if min_ == 1000000:
            answer.append(-1)
        else:
            answer.append(min_)
                
    return answer
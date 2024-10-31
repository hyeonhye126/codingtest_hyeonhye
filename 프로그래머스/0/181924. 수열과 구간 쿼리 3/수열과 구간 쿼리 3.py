def solution(arr, queries):
    answer = []
    
    for query in queries:
        i = query[0]
        j = query[1]

        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        
    answer = arr
    return answer
def solution(arr, queries):
    answer = []
    
    for li in queries:
        i = li[0]
        j = li[1]

        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        
    answer = arr
    return answer
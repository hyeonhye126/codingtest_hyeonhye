def solution(arr):
    if 2 not in arr:
        return [-1]
    
    first_index = arr.index(2)
    last_index = len(arr) - 1 - arr[::-1].index(2)
    
    return arr[first_index:last_index + 1]
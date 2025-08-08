def solution(dots):
    def is_parallel(a, b, c, d):
        if (b[0] - a[0]) * (d[1] - c[1]) == (d[0] - c[0]) * (b[1] - a[1]): return 1;
        elif (c[0] - a[0]) * (d[1] - b[1]) == (d[0] - b[0]) * (c[1] - a[1]): return 1;
        elif (d[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (d[1] - a[1]): return 1; 
        else: return 0;
    
    answer = is_parallel(dots[0], dots[1], dots[2], dots[3])
    return answer
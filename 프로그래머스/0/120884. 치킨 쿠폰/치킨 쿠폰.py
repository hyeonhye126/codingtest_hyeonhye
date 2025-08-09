def solution(chicken):
    coupons = chicken
    service = 0
    
    while coupons >= 10:
        new = coupons // 10
        service += new
        coupons = new + coupons % 10
    
    return service
from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counter = Counter(dice) # 딕셔너리
    
    if len(counter) == 1:
        p = dice[0]
        return p * 1111
    
    elif len(counter) == 2:
        for num, cnt in counter.items():
            if cnt == 3:
                p = num
            else:
                q = num
                
        if 'p' in locals(): # 3 + 1 패턴
            return (10 * p + q) ** 2
        else: # 2 + 2 패턴
            nums = list(counter.keys())
            return (nums[0] + nums[1]) * abs(nums[0] - nums[1])
        
    
    elif len(counter) == 3:
        for num, cnt in counter.items():
            if cnt == 2:
                p = num
            else:
                others = [n for n, c in counter.items() if c == 1]
        return others[0] * others[1]
        
    else:
        return min(dice)
    
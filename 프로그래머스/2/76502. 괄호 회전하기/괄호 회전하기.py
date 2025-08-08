def solution(s):
    answer = 0
    
    for i in range (len(s)):
        rotated = s[i:] + s[:i]
        stack = []
        flag = 1
        
        for ch in rotated:
            if ch in '[({':
                stack.append(ch)
            else:
                if not stack:
                    flag = 0
                    break
                top = stack.pop()
                if ch == ']' and top != '[':
                    flag = 0
                if ch == '(' and top != ')':
                    flag = 0
                if ch == '{' and top != '}':
                    flag = 0
                    
        if stack:
            flag = 0
        
        if flag:
            answer += 1
    
    return answer
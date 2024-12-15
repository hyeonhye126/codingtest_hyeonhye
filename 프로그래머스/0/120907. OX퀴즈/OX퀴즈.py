def solution(quiz):
    answer = []
    
    for q in quiz:
        eq = q.split()
        op = eq[1]
        
        if op == '+':
            if int(eq[0]) + int(eq[2]) == int(eq[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(eq[0]) - int(eq[2]) == int(eq[4]):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer
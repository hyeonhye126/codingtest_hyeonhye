def solution(binomial):
    li = list(binomial.split(" "))
    
    a = int(li[0])
    b = int(li[2])
    op = li[1]
    answer = 0
    
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "*":
        answer = a * b
    
    return answer
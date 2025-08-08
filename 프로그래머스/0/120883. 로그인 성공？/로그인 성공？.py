def solution(id_pw, db):
    result = ''
    
    for i, p in db:
        if i == id_pw[0] and p == id_pw[1]:
            return "login"
        elif i == id_pw[0] and p != id_pw[1]:
            return "wrong pw"
    
    return "fail"
def solution(money):    
    coffee = money // 5500
    rest_money = money % 5500
    answer = [coffee, rest_money]
    return answer
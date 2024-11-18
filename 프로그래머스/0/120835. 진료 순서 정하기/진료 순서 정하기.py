def solution(emergency):
    return [sorted(emergency, reverse=True).index(num) + 1 for num in emergency]
from collections import deque

def solution(cards1, cards2, goal):
    d1, d2 = deque(cards1), deque(cards2)
    for w in goal:
        if d1 and d1[0] == w:
            d1.popleft()
        elif d2 and d2[0] == w:
            d2.popleft()
        else:
            return "No"
    return "Yes"
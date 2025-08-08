def solution(score):
    average = []
    for s in score:
        average.append((s[0] + s[1]) / 2)
    
    rank = []
    for i in range(len(average)):
        cnt = 0
        for j in range(len(average)):
            if average[i] < average[j]:
                cnt += 1
        rank.append(cnt + 1)
        
    return rank
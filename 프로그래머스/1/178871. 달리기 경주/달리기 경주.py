def solution(players, callings):
    
    pos = {name:i for i, name in enumerate(players)}
    
    for c in callings:
        i = pos[c]
        if i == 0:
            continue
        
        front = players[i-1]
        
        players[i], players[i-1] = players[i-1], players[i]
        
        pos[c] = i - 1
        pos[front] = i
        
        
    return players
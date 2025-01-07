def solution(keyinput, board):
    start = [0, 0]
    
    for k in keyinput:
        # if abs(start[0]) == board[0] // 2 or abs(start[1]) == board[1] // 2:
        #     continue
        
        if k == "left":
            if start[0] != -(board[0] // 2):
                start[0] -= 1
        elif k == "right":
            if start[0] != board[0] // 2:
                start[0] += 1
        elif k == "down":
            if start[1] != -(board[1] // 2):
                start[1] -= 1
        else:
            if start[1] != board[1] // 2:
                start[1] += 1
    
    return start
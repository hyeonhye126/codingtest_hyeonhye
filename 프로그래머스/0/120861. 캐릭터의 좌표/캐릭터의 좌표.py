def solution(keyinput, board):
    position = [0, 0]
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for k in keyinput:
        if k == "left":
            if position[0] > -max_x:
                position[0] -= 1
        elif k == "right":
            if position[0] < max_x:
                position[0] += 1
        elif k == "down":
            if position[1] > -max_y:
                position[1] -= 1
        else:
            if position[1] < max_y:
                position[1] += 1
    
    return position
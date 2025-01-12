def solution(board):
    n = len(board)
    
    danger_zone = [[0] * n for _ in range(n)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                danger_zone[r][c] = 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        danger_zone[nr][nc] = 1
    
    safe_count = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0 and danger_zone[r][c] == 0:
                safe_count += 1

    return safe_count
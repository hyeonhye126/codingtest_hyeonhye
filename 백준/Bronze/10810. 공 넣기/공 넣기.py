N, M = map(int, input().split())

board = [0] * N 

for _ in range (M):
    i, j, k = map(int, input().split())
    board[i-1:j] = [k] * (j - i + 1)

answer = ' '.join(map(str, board))
print(answer)
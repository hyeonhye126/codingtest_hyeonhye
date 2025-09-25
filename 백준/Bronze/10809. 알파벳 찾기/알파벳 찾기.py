S = input()

board = [-1] * 26

for i in range(len(S)):
    ch = S[i]
    idx = ord(ch) - ord('a')

    if board[idx] == -1:
        board[idx] = i

print(' '.join(map(str, board)))
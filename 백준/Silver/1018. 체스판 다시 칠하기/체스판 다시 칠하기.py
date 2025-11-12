N, M = map(int, input().split())

chess = [list(input().strip()) for _ in range(N)]

def count_repaint(x, y):
    repaint_w = 0
    repaint_b = 0

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            current = chess[i][j]
            if (i + j) % 2 == 0: # 짝수
                if current != 'W':
                    repaint_w += 1
                if current != 'B':
                    repaint_b += 1
            else: # (i + j) % != 0 홀수
                if current != 'B':
                    repaint_w += 1
                if current != 'W':
                    repaint_b += 1

    return min(repaint_w, repaint_b)

answer = 64 # 8 * 8 최대 칸 수
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        answer = min(answer, count_repaint(i, j))

print(answer)
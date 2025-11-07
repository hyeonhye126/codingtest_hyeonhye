from collections import deque

N = int(input())
dq = deque()

for i in range (N, 0, -1):
    dq.appendleft(i) # 역방향에서 꺼낸 i를 되돌려 둔다
    dq.rotate(i) # 오른쪽 1칸 회전

print(' '.join(map(str, dq)))
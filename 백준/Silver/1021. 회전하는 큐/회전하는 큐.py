from collections import deque

N, M = map(int, input().split()) # N: 큐의 크기 M: 뽑아내려고 하는 수의 개수
targets = list(map(int, input().split())) # 뽑아내려고 하는 원소의 위치

dq = deque(range(1, N + 1))
ops = 0

for x in targets:
    pos = dq.index(x) # 현재 위치

    # 어느 방향이 더 적게 도는지 결정
    if pos <= len(dq) // 2:
        # 왼쪽 회전 pos번
        dq.rotate(-pos)
        ops += pos
    else:
        # 오른쪽 회전 len - pos번
        r = len(dq) - pos
        dq.rotate(r)
        ops += r

    # 맨 앞이 x이므로 뽑기 (비용 0)
    dq.popleft()

print(ops)
import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x:(x[1], x[0])) # end 오름차순 정렬

count = 0
last_end = -1
for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
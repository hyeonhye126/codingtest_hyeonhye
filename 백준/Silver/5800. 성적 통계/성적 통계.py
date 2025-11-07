k = int(input())

for i in range (k):
    num_list = list(map(int, input().split()))
    
    nums = num_list[0]
    scores = num_list[1:]

    max_score = max(scores)
    min_score = min(scores)

    # 내림차순 정렬
    scores.sort(reverse=True)

    # 인접한 점수 차이 구하기
    diffs = []
    for j in range(len(scores) - 1):
        diffs.append(scores[j] - scores[j+1])
    gap = max(diffs)

    print("Class %d" %(i + 1))
    print("Max %d, Min %d, Largest gap %d" %(max_score, min_score, gap))
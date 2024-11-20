def solution(num_list, n):
    tmp_list, answer, cnt = [], [], 0
    for c in num_list:
        tmp_list.append(c)
        cnt += 1
        if cnt == n:
            answer.append(tmp_list)
            tmp_list, cnt = [], 0
    return answer
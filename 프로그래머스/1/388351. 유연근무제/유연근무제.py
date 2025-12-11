def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        time = schedules[i] + 10 # 출근 해야하는 시간
        if time % 100 >= 60:
            time += 100
            time -= 60
        
        flag = True
        for j in range(len(timelogs[i])):
            day = (startday + j - 1) % 7 + 1
            if day == 6 or day == 7: # 토요일, 주말은 제외
                continue
            else:
                if (time < timelogs[i][j]): # 출근해야하는 시각보다 실제 출근 시각이 늦으면 False
                        flag = False
                        break
        
        if flag:
            answer += 1
    
    return answer
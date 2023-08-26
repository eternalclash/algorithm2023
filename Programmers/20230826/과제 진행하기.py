def solution(plans):
    def plusClock(clock,plusTime) :
        clock = clock.split(":")
        minute = int(clock[1]) + int(plusTime)
        hour = int(clock[0])*60
        return hour+minute
    answer = []
    now = []
    stop = []
    
    #계획 시간대로 정렬
    plans.sort(key= lambda x : x[1])
    
    for plan in plans:
        name,start,playtime = plan
        if len(now) == 0 :
            now.append(plan)
        else:
            now_name,now_start,now_playtime = now.pop()
            nowClock = plusClock(now_start,now_playtime)
            startClock = plusClock(start,0)
            restClock = nowClock -startClock
            if restClock > 0:
                stop.append([now_name,now_start,restClock])
                now.append(plan)
            elif restClock == 0:
                answer.append(now_name)
                now.append(plan)
            else :
                answer.append(now_name)
                restTime = -1 * restClock
                while stop :
                    stop_name,stop_start,stop_playtime = stop.pop()
                    if stop_playtime > restTime : 
                        stop.append([stop_name,stop_start,stop_playtime-restTime])
                        break
                    else :
                        answer.append(stop_name)
                        restTime -= stop_playtime                 
                now.append(plan)
    answer.append(now.pop()[0])
    while stop :
        answer.append(stop.pop()[0])
    return answer
def solution(targets):
    answer = 0
    prev = -1
    targets.sort(key=lambda x : x[1])
    for target in targets:
        start,end = target
        if prev <= start :
            answer+=1
            prev = end
    
    return answer



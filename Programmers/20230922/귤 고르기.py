def solution(k, tangerine):
    #서로 다른 종류의 수를 최소화
    answer = 0
    obj = {}
    for x in tangerine:
        if x in obj :
            obj[x] += 1
        else:
            obj[x] = 1
    arr = list(obj.values())
    
    arr.sort(reverse=True)
    for x in arr :
        answer += 1
        k -= x
        if k <= 0:
            return answer
def solution(picks, minerals):
    if sum(picks) == 0 :
        return 0
    if sum(picks)*5 < len(minerals) :
        minerals = minerals[:sum(picks)*5]
    minerals_amount = []
    arr = [0]*3
    for i in range(len(minerals)):
        if i !=0 and i % 5 == 0:
            minerals_amount.append(arr)
            arr = [0] * 3
            if minerals[i] == "diamond" :
                arr[0]+=1
            elif minerals[i] == "iron" :
                arr[1]+=1
            else :
                arr[2]+=1
        else :
            if minerals[i] == "diamond" :
                arr[0]+=1
            elif minerals[i] == "iron" :
                arr[1]+=1
            else :
                arr[2]+=1
        if i == len(minerals)-1 :
            minerals_amount.append(arr)
    minerals_amount.sort(key = lambda x : (-x[0],-x[1]))
    answer = 0
    k = 0
    for i in range(3):
        while picks[i]>0 and len(minerals_amount) > k:
            if i == 0 :
                answer += minerals_amount[k][0] + minerals_amount[k][1] + minerals_amount[k][2]
            elif i == 1 :
                answer += minerals_amount[k][0]*5 + minerals_amount[k][1] + minerals_amount[k][2]
            else :
                answer += minerals_amount[k][0]*25 + minerals_amount[k][1]*5 + minerals_amount[k][2]               
            k+=1
            picks[i]-=1

    return answer
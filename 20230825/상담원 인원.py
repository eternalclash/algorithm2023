from itertools import combinations_with_replacement,permutations
import heapq
def solution(k, n, reqs):
    answer = 0
    cases = set()
    def findMento() :
        for mentos in combinations_with_replacement([i for i in range(1,n-k+2)],r=k):
            if sum(mentos) == n:
                for permutation in permutations(mentos,k) :
                    cases.add(permutation)
    participants = [[] for _ in range(k)]
    for req in reqs:
        participants[req[2]-1].append([req[0],req[0]+req[1]])
    findMento()
    def countTime(mentees,mento):
        schedule = [0]*mento
        waiting_time = 0
        heapq.heapify(schedule)
        for mentee in mentees:
            end_time = heapq.heappop(schedule)
            if end_time <=  mentee[0]:
                heapq.heappush(schedule,mentee[1])
            else:
                late_time = end_time - mentee[0]
                waiting_time = waiting_time + late_time
                heapq.heappush(schedule,mentee[1]+late_time)                           
        return waiting_time              
    answer = 100000000                          
    for case in cases:
        time = 0
        for i in range(k):
                time = time + countTime(participants[i],case[i])
        answer = min(answer,time)
    return answer
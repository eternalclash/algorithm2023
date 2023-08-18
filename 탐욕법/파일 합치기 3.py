import heapq
T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int,input().split()))
    heapq.heapify(arr)
    answer = 0
    while len(arr) != 1:
        x = heapq.heappop(arr)
        y = heapq.heappop(arr)
        answer += x + y
        heapq.heappush(arr,x+y)
    print(answer)
    

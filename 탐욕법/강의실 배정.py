import heapq
N = int(input())
arr =[]
for _ in range(N):
    start,end = map(int,input().split())
    arr.append([start,end])

arr.sort()
room = []
heapq.heappush(room,arr[0][1])
for i in range(1,N):
    if arr[i][0] < room[0] :
        heapq.heappush(room,arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,arr[i][1])
print(len(room))


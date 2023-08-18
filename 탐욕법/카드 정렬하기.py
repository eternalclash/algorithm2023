import heapq
N = int(input())
arr= []
for _ in range(N):
    arr.append(int(input()))
heapq.heapify(arr)
count = 0
while len(arr) != 1:
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    count += x + y
    heapq.heappush(arr,x+y)
print(count)
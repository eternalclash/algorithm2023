import sys
import heapq
N, M, X = map(int,input().split())
INF = sys.maxsize

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start,end,T = map(int,input().split())
    graph[start].append([T,end])
def dijkstra(start) :
    distance = [INF] * (N+1)
    q = []
    distance[start] = 0
    heapq.heappush(q,[0,start])
    while q:
        time,start = heapq.heappop(q)
        if distance[start] < time:
             continue
        for next in graph[start]:
            next_time,next_start = next
            next_time += time
            if next_time < distance[next_start]:
                distance[next_start] = next_time
                heapq.heappush(q,[next_time,next_start])
    return distance

answer = dijkstra(X)

for i in range(1,N+1) :
    if i != X:
        temp = dijkstra(i)
        answer[i] += temp[X]
print(max(answer[1:]))
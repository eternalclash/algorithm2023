import sys
import heapq
n,m,r = map(int,input().split()) # 지역의 개수 n, 예은이의 수색범위 m, 길의 개수 r
item = [0]+list(map(int,input().split()))
INF = sys.maxsize
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    graph[a].append([l,b])
    graph[b].append([l,a])

def dijkstra (start) :
    heap = []
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    heapq.heappush(heap,[0,start])
    while heap:
        weight,node = heapq.heappop(heap)
        if weight > distance[node] :
            continue
        for next in graph[node]:
            next_weight,next_node = next
            next_weight+=weight
            if next_weight < distance[next_node]:
                distance[next_node] = next_weight
                heapq.heappush(heap,[next_weight,next_node])
    return distance
max_value = int(-1e9)
for i in range(1,n+1):
    temp = 0
    result = dijkstra(i)

    for j in range(1,n+1):
        if result[j] <=m :
            temp += item[j]
    max_value = max(max_value,temp)
print(max_value)
    



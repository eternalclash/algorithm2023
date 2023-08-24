from collections import deque
N, K = map(int,input().split())
max_size = 100001
visited = [-1] * 100001
visited[N] = 0
q = deque()
q.append(N)
while q:
    start = q.popleft()
    if start == K :
        print(visited[K])
        break
    if start*2<max_size and (visited[start*2] == -1 or (visited[start*2]<visited[start])):
        visited[start*2] = visited[start]
        q.appendleft(start*2)
    for walk in [start-1,start+1]:
        if 0<=walk<max_size and (visited[walk]== -1 or visited[walk] > visited[start]):
            visited[walk] = visited[start] + 1
            q.append(walk)
   
        
    
    

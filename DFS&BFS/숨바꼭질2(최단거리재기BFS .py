from collections import deque
N , K = map(int,input().split())
max_size = 100001
visited = [-1] * max_size
q = deque()
q.append(N)
time = 0
kind = 0
visited[N] = 0
while q :
    now = q.popleft()
    if now == K :
        kind += 1
    for after in [now*2,now+1,now-1]:
        if 0<=after<max_size:
            if visited[after] == -1:
                visited[after] = visited[now] + 1
                q.append(after)
            else:
                if visited[now] < visited[after]:
                    visited[after] = visited[now] + 1
                    q.append(after)
   


print(visited[K])
print(kind)
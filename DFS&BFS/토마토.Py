from collections import deque
import sys
M,N = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
directions = [[1,0],[0,1],[-1,0],[0,-1]]
time = 0
q= deque()
def bfs():
    while q :
            x,y,step = q.popleft()
            for direction in directions:
                dx = x + direction[0]
                dy = y + direction[1]
                if 0<=dx<N and 0<=dy<M and arr[dx][dy] == 0 :
                    arr[dx][dy] = step + 1
                    q.append((dx,dy,step+1))
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j,1))
bfs()
max = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            sys.exit(0)
        else :
            if arr[i][j] > max :
                max = arr[i][j]

print(max-1)
                    
    


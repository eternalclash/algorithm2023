import sys
from collections import deque
N = int(input())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
visited1 = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]
q1 = deque()
q2 = deque()
directions = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs1(q) :
    while q:
        x,y,color = q.popleft()
        for direction in directions:
            dx = x + direction[0]
            dy = y + direction[1]
            if 0<=dx<N and 0<=dy<N and arr[dx][dy] == color and not visited1[dx][dy]:
                visited1[dx][dy] = True
                q1.append((dx,dy,color))
def bfs2(q,isSak) :
    if isSak :
        while q:
            x,y = q.popleft()
            for direction in directions:
                dx = x + direction[0]
                dy = y + direction[1]
                if 0<=dx<N and 0<=dy<N and arr[dx][dy] != "B" and not visited2[dx][dy]:
                    visited2[dx][dy] = True
                    q2.append((dx,dy))
    else :
        while q:
            x,y = q.popleft()
            for direction in directions:
                dx = x + direction[0]
                dy = y + direction[1]
                if 0<=dx<N and 0<=dy<N and arr[dx][dy] == "B" and not visited2[dx][dy]:
                    visited2[dx][dy] = True
                    q2.append((dx,dy))



count1  = 0
count2  = 0                
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            visited1[i][j]= True
            q1.append((i,j,arr[i][j]))
            bfs1(q1)
            count1 += 1
        if not visited2[i][j]: 
            visited2[i][j] = True
            q2.append((i,j))
            if arr[i][j] == "R" or arr[i][j]=="G":
                bfs2(q2,True)
            else:
                bfs2(q2,False)
            count2 += 1
print(count1, end=" ")
print(count2)
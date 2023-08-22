import sys
from collections import deque
R,C = map(int,input().split())
directions = [[1,0],[0,1],[-1,0],[0,-1]]
graph = []
for _ in range(R):
    graph.append(list(input()))
q = deque()
def bfs () :
    while q:
        x,y,who,cnt = q.popleft()
        if who=="J" and graph[x][y] != "J" : continue
        if (x == 0 or x == R - 1 or y == 0 or y == C-1 )and graph[x][y]=="J":
            return cnt +1
        for direction in directions:
            dx = x + direction[0]
            dy = y + direction[1]
            if who == "J":
                if 0<=dx<R and 0<=dy<C and graph[dx][dy] == ".":
                    graph[dx][dy] = "J"
                    q.append([dx,dy,"J",cnt+1])
 
            else:
                if 0<=dx<R and 0<=dy<C and (graph[dx][dy] == "." or graph[dx][dy] == "J"):
                    q.append([dx,dy,"F",cnt+1])      
                    graph[dx][dy] = "F"     
    return -1
for i in range(R):
    for j in range(C):
        if graph[i][j] == "J":
            if i==0 or i == R-1 or j==0 or j==C-1:
                print(1)
                sys.exit(0)
            q.appendleft([i,j,"J",0])
        if graph[i][j] == "F":
            q.append([i,j,"F",0])
answer = bfs()
if answer == -1 :
    print("IMPOSSIBLE")
else:
    print(answer)



                






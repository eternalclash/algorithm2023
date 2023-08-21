from collections import deque
import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

directions = [[1,0],[0,1],[-1,0],[0,-1]]
q= deque([])
def bfs() :
    count = 1
    while q :
        x,y = q.popleft()
        for direction in directions:
            dx = x + direction[0]
            dy = y + direction[1]
            if 0<=dx<N and 0<=dy<N and arr[dx][dy] == 1:
                q.append((dx,dy))
                arr[dx][dy] = 0
                count += 1
    return count
answer = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            q.append((i,j))
            arr[i][j]=0
            answer.append(bfs())

answer.sort()
print(len(answer))
for x in answer:
    print(x)
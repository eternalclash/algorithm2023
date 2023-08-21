from collections import deque
M, N = map(int,input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))
visited = [[-1]*N for _ in range(M)]
directions = [(1,0),(0,1),(0,-1),(-1,0)]
q = deque()
count = 0
def dfs(x,y,num) :
    global count
    if x==M-1 and y==N-1 :
        return 1
    if visited[x][y] != -1 :
        return visited[x][y]
    visited[x][y] = 0
    for direction in directions:
        dx = x + direction[0]
        dy = y + direction[1]
        if 0<=dx<M and 0<=dy<N and arr[dx][dy] < num:
            visited[x][y]+=dfs(dx,dy,arr[dx][dy])
    return visited[x][y]
print(dfs(0,0,arr[0][0]))

    
from collections import deque
import sys

input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [list(0 for _ in range(N)) for _ in range(N)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]
babyLevel = 2
px, py = 0,0
result = 0
consume = 0
def bfs(x,y) :
    global babyLevel
    visited = [list(0 for _ in range(N)) for _ in range(N)]
    que = deque()
    que.append([x,y])
    visited[x][y] = 1


    while que :
        
        x,y = que.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 :
                if babyLevel >= board[nx][ny] :
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx,ny])

                    if 0 < board[nx][ny] < babyLevel :
                        board[nx][ny] = 0
                        # print("here")
                        # print("visited : " + str(visited))
                        # print("board : " + str(board))
                        # print("nx: " + str(nx) + " ny:" + str(ny) + " temp:"+str(visited[nx][ny] - 1)+ " level:"+str(babyLevel))
                        
                        #food.append([visited[nx][ny] - 1, nx, ny])
                        #print(food)
            
                        return [nx, ny, visited[nx][ny] - 1]

9
    
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 9 :
            px,py = i,j
            board[i][j] = 0

while True :
    flag = True
    
    for i in range(N) :
        for j in range(N) :
            if 0 < board[i][j] < babyLevel :
                flag = False
    
    if flag :
        print(board)
        print()
        print(result)
        break
    
    if not flag :
        px, py, temp = bfs(px,py)
        print(px,py,temp,board[px][py],babyLevel)
        result += temp
        consume += 1
    
    if consume == babyLevel :
        consume = 0
        babyLevel += 1
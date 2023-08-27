from collections import deque
def solution(board):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    q= deque()
    visited = [[987654321] * len(board[0]) for _ in range(len(board))]
    def bfs () :
        while q:
            x,y = q.popleft()
            # if board[x][y] == "G" : return visited[x][y]
            for direction in directions:
                dx = x
                dy = y
                while True :
                    dx += direction[0]
                    dy += direction[1]
                    if 0<=dx<len(board) and 0<=dy<len(board[0]) and board[dx][dy] == "D":
                        dx-= direction[0]
                        dy-= direction[1]
                        break
                    if dx<0 or dx>=len(board) or dy< 0 or dy>=len(board[0]):
                        dx-= direction[0]
                        dy-= direction[1]
                        break
                if board[dx][dy] == "G": 
                    return visited[x][y] + 1
                if visited[x][y] < visited[dx][dy] :
                    visited[dx][dy] = visited[x][y]+1
                    q.append((dx,dy))
            
        return -1
                    
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R" :
                visited[i][j] = 0
                q.append((i,j))
                return bfs()

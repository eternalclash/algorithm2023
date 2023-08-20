import sys
arr = []
for _ in range(19):
    arr.append(list(map(int,input().split())))
direction = [(1,0),(0,1),(1,1),(-1,1)]
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1 or arr[i][j] == 2:
            board = arr[i][j]
            for x in range(4):
                dx = i + direction[x][0]
                dy = j + direction[x][1]
                cnt = 1
                while 0<=dx<=18 and 0<=dy<=18 and arr[dx][dy] == board:
                    cnt +=1
                    dx+=direction[x][0]
                    dy+=direction[x][1]
                if cnt == 5:
                    if 0 <= i - direction[x][0] < 19 and 0 <= j - direction[x][1] < 19 and arr[i - direction[x][0]][j - direction[x][1]] == board:
                        break
                    # if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == focus:
                    #     break
                    print(board)
                    print(i+1,j+1)
                    sys.exit(0)
print(0)

                            



N,M,R = map(int,input().split())  # [N][M] #R 회전의 수
arr = [] 
for _ in range(N):
    arr.append(list(map(int,input().split())))
for _ in range(R):
    for i in range(min(N,M)//2):
        x,y = i,i
        value = arr[x][y]
        for j in range(i+1,N-i):
            x = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp
        for j in range(i+1,M-i):
            y = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp
        for j in range(N-i-2,i-1,-1):
            x = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp
        for j in range(M-i-2,i-1,-1):
            y = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp    
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()



N, M = map(int,input().split())
train = [[0] * 20 for _ in range(N)]
for _ in range(M):
    arr= list(map(int,input().split()))
    if arr[0]==1:
        if train[arr[1]-1][arr[2]-1] == 1:
            continue
        else :
            train[arr[1]-1][arr[2]-1] = 1
    elif arr[0]==2:
        train[arr[1]-1][arr[2]-1] = 0
    elif arr[0]==3:
        train[arr[1]-1].pop()
        train[arr[1]-1].insert(0,0)
    elif arr[0]==4:
        train[arr[1]-1].pop(0)
        train[arr[1]-1].append(0)
print(len(set(tuple(element) for element in train)))
    

           


import copy
T = int(input())
for _ in range(T):
    n,d = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    dae = [arr[i][i] for i in range(n)]
    bu = [arr[i][n-1-i] for i in range(n)]
    ga = [arr[(n-1)//2][i] for i in range(n)]
    se = [arr[i][(n-1)//2] for i in range(n)]
    
    count = abs(d)//45
    minus = False
    if d < 0 :
        minus = True
    for _ in range(count) :
        if not minus:
            tmp = copy.deepcopy(ga)
            ga = copy.deepcopy(bu)
            bu = copy.deepcopy(se)
            se = copy.deepcopy(dae)
            dae = copy.deepcopy(tmp)
            ga.reverse()
        else :
            tmp = copy.deepcopy(ga)
            ga = copy.deepcopy(dae)
            dae = copy.deepcopy(se)
            se = copy.deepcopy(bu)
            bu = copy.deepcopy(tmp)
            bu.reverse()
    for i in range(n):
        arr[i][i] = dae[i]
        arr[i][n-1-i] = bu[i]
        arr[(n-1)//2][i] = ga[i]
        arr[i][(n-1)//2] = se[i]
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
    # 대각선, 부각선, 가로, 세로
    
            
    # arr[2][0] arr[2][1] arr[2][2] arr[2][3] arr[2][4]
    #  arr[(n-1)//2][i]
    # arr[0][0] arr[1][1] arr[2][2] arr[3][3] arr[4][4]
    #  arr[i][i]
    # arr[0][2] arr[1][2] arr[2][2] arr[3][2] arr[4][2]
    #  arr[i][(n-1)//2]
    # arr[0][4] arr[1][3] arr[2][2] arr[3][1] arr[4][0]
    #  arr[i][n-1-i]


import heapq
N = int(input())
arr = []
calandar= [0]*366
for _ in range(N):
    x,y = map(int,input().split())
    for i in range(x,y+1):
        calandar[i]+=1
row = 0
column = 0
answer = 0
for i in range(len(calandar)):
    if calandar[i] != 0:
        row = max(row,calandar[i])
        column+=1
    else:
        answer+= row*column
        row = 0
        column = 0
if row!= 0 : answer+=row*column
print(answer)


        

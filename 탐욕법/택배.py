N,C = map(int,input().split())
M = int(input())
answer = 0
arr = []
for _ in range(M):
    start,end,amount = map(int,input().split())
    arr.append([start,end,amount])
box = [0 for _ in range(N+1)]
# 받는 마을번호, 보내는 마을번호 정렬
arr.sort(key = lambda x: (x[1],x[0]) )

for i in range(M):
    # start,end,amount 가져오기
    start = arr[i][0]
    end = arr[i][1]
    totalBox = arr[i][2]
    for j in range(start,end):
        totalBox = min(totalBox,C-box[j])
    for j in range(start,end):
        box[j] += totalBox
    answer += totalBox
print(answer)


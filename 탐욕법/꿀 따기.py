N = int(input())
arr = list(map(int,input().split()))

# 9 9 4 1 4 9 9
# 4 1 4 9 9
# 4 1 4 9 9
# greedy는 케이스를 잘 쪼개야한다
# 16m 56s
sum = sum(arr[:])
answer = 0
temp = arr[0]
for i in range(1,N) :
    temp += arr[i]
    answer = max(answer, sum - arr[0]-arr[i] + sum - temp)

arr.reverse()
temp = arr[0]
for i in range(1,N):
    temp += arr[i]
    answer = max(answer, sum - arr[0]-arr[i] + sum - temp)    

for i in range(1,N-1):
    answer = max(answer, sum - arr[0] - arr[-1] + arr[i])
print(answer)
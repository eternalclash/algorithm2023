H,W = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
for i in range(1,W-1):
    max_height = min(max(arr[:i]),max(arr[i:]))
    if arr[i] <= max_height:
        answer +=max_height-arr[i]
print(answer)

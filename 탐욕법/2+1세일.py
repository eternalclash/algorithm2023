N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
sum = 0
for i in range(N):
    if (i+1) % 3 == 0 :
        continue
    else:
        sum += arr[i]

print(sum)
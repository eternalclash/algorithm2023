N = int(input())
count = 0
arr = []
for i in range(1,N+1):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(N) :
    tip = arr[i] - i
    if tip > 0:
       count += arr[i] - i

print(count)

    

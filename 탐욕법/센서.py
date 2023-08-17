N = int(input())
K = int(input())
arr = list(map(int,input().split()))
arr.sort()
diff = []
for i in range(0,N-1):
    diff.append(arr[i+1]-arr[i])
diff.sort()
if K >= 2:
  for i in range(K-1):
      diff.pop()
print(sum(diff))
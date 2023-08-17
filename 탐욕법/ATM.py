N = int(input())
data = list(map(int, input().split()))
data.sort()
sum = 0
plus = 0
for i in range(N):
    plus += data[i] + sum
    sum += data[i]

print(plus)


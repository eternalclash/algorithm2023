n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

m.sort(reverse=True) # 내림차순으로 정렬
result = []

for j in range(n):
    result.append(m[j]*(j+1))
print(max(result))
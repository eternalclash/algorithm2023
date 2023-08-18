N = int(input())
c = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))
c.sort(reverse=True)
b.sort(reverse=True)
count = 0
if b[0] > c[0] :
    print(-1)
else:
    while b :
        for x in c:
            for y in b:
                if x >= y:
                    b.remove(y)
                    break
        count += 1
    print(count)

#14m15s
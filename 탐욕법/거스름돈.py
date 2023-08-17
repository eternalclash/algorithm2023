import sys
N = int(sys.stdin.readline())
coin_types = [5,2]
count = 0
restMoney = N % 5
if N in [1,3] :
    result = -1
elif restMoney in [2,4] :
    result = N//5+restMoney//2
else :
    result = N//5-1+(restMoney+5)//2

print(result)





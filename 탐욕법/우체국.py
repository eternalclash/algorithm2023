N=int(input())
vilage=[[]for _ in range(N)]

po=0
for i in range(N):
    X,A=map(int,input().split())
    vilage[i]=[X,A]
    po+=A
now=0
vilage.sort(key=lambda x:(x[0]))
for i in range(N):
    now+=vilage[i][1]
    if now>=po/2:
        print(vilage[i][0])
        break

#거리를 중심으로 구하지만
#인구가 많으면 많을수록 거리값이 가산
#그래서 인구가산이 가장 적은 지역을 구하면 된다
#8m45s

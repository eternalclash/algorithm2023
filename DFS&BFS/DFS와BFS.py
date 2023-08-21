from collections import deque
N,M,V = map(int,input().split())
graph = [[False]*(N + 1) for _ in range(N + 1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def dfs(V):
    visited1[V] = True
    print(V,end=" ")
    for i in range(1, N + 1):
        if visited1[i] == False and graph[V][i] == True:
            dfs(i)
def bfs(V):
    visited2[V] = True
    print(V,end=" ")
    q= deque([V])
    while q :
        x = q.popleft()
        for i in range(1,N+1):
            if visited2[i]== False and graph[x][i] :
                visited2[i] = True
                q.append(i)
                print(i,end=" ")
        

    
dfs(V)
print()
bfs(V)
K = int(input())
def dfs(i):
    global result 
    for node in graph[i]:
        if visited[node] == -1:
            if visited[i] == 1:
                visited[node] = 2
            if visited[i] == 2:
                visited[node] = 1
            dfs(node)
        else :
            if visited[node] == visited[i]:
                result = False 
                return             
    return
for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v  = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [-1] * (V+1)
    result = True    
    for i in range(1,V+1):
        if visited[i] == -1:
            visited[i] = 1
            dfs(i)
            if result == False:
                break
    if result == False:
        print("NO")
    else:
        print("YES")
    


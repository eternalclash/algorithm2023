N = str(input())
min_value = 99999
max_value = 0
def count_odd (arr):
    count = 0
    for i in range(len(arr)):
        if int(arr[i])%2 != 0:
            count+=1
    return count

def dfs(N,count) :
    global min_value,max_value
    count = count + count_odd(N)
    if len(N) == 1:
        min_value = min(min_value,count)
        max_value = max(max_value,count)
        return
    elif len(N) == 2:
        N = int(N)//10 + int(N)%10
        dfs(str(N),count)
    else :
        for i in range(1,len(N)):
            for j in range(i+1,len(N)):
                temp = int(N[:i])+int(N[i:j])+int(N[j:])
                dfs(str(temp),count)
dfs(N,0)
print(min_value,max_value)



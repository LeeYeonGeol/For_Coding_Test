n = int(input())

ch=[0]*(n+1)

def dfs(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end= " ")
        print()
        return
    else:
        ch[v]=1
        dfs(v+1)
        ch[v]=0
        dfs(v+1)

dfs(1)


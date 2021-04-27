n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

ans = 0

def dfs(arr):
    global ans
    sub = 0
    if len(arr) == n*m:

        narr = []
        for i in range(n):
            narr.append(arr[i*m:i*m+m])

        # 가로
        for i in range(n):
            aa = 0
            for j in range(m):
                if narr[i][j] == 0:
                    aa = aa * 10 + graph[i][j]
                else:
                    sub += aa
                    aa = 0
            sub += aa
            aa = 0
        # 세로
        for j in range(m):
            bb = 0
            for i in range(n):
                if narr[i][j] == 1:
                    bb = bb*10 + graph[i][j]
                else:
                    sub += bb
                    bb = 0
            sub += bb
            bb = 0
        ans = max(ans,sub)
        return
    else:
        dfs(arr+[0])
        dfs(arr+[1])

dfs([])
print(ans)
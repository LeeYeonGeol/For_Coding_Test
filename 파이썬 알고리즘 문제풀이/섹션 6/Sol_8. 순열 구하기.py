n, k = map(int, input().split())

ans = 0
arr = []
def dfs(cnt):
    global ans
    if cnt == k:
        ans += 1
        for i in arr:
            print(i, end= " ")
        print()
        return
    else:
        for i in range(1, n+1):
            if not i in arr:
                arr.append(i)
                dfs(cnt+1)
                arr.pop()
dfs(0)
print(ans)
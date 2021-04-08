n, m = map(int, input().split())


ans = []
ans2 = 0
def dfs(start, cnt):
    global ans2
    if cnt == m:
        for i in ans:
            print(i, end=' ')
        print()
        ans2 += 1
        return
    else:
        for i in range(start+1, n+1):
            ans.append(i)
            dfs(i, cnt+1)
            ans.pop()

dfs(0, 0)
print(ans2)
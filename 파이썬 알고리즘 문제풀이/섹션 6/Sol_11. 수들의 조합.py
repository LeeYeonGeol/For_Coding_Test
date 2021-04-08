n, k = map(int, input().split())

arr = list(map(int, input().split()))

m = int(input())

ans = []
ans2 = 0
def dfs(start, cnt):
    global ans2
    if cnt == k:
        if sum(ans) % m == 0:
            ans2 += 1
        return
    else:
        for i in range(start, n):
            ans.append(arr[i])
            dfs(i+1, cnt+1)
            ans.pop()

dfs(0,0)
print(ans2)
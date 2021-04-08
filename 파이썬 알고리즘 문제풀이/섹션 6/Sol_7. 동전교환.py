import sys
n = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

target = int(input())

ans = int(1e9)

def dfs(price, cnt):
    global ans
    if cnt > ans:
        return

    if price > target:
        return
    elif price == target:
        ans = min(ans,cnt)
        return
    else:
        for i in arr:
            dfs(price+i, cnt+1)

dfs(0, 0)
print(ans)

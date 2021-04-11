n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))


ans = int(1e9)
def dfs(L):
    global ans
    if L == n:
        if len(a) == len(set(a)):
            ans = min(ans, max(a)-min(a))
        return
    else:
        for i in range(3):
            a[i] += arr[L]
            dfs(L+1)
            a[i] -= arr[L]


a = [0,0,0]
dfs(0)
print(ans)
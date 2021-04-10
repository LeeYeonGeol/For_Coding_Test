n = int(input())

arr = list(map(int ,input().split()))

#arr.sort()

ans = [False]*(sum(arr)+1)
ans[0] = True
result = set()


def dfs(v, sum):

    if v == n:
        if sum > 0:
            ans[sum] = True
        return
    else:
        dfs(v+1, sum+arr[v])
        dfs(v+1, sum-arr[v])
        dfs(v+1, sum)

dfs(0, 0)
print(ans.count(False))


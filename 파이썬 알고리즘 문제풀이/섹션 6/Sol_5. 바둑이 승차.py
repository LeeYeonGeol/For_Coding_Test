c, n = map(int, input().split())


result = -int(1e9)
arr = []
for _ in range(n):
    arr.append(int(input()))

total = sum(arr)

def DFS(L, sum, tsum):
    global result
    if sum>c:
        return
    if total-tsum + sum < result:
        return

    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+arr[L], tsum+arr[L])
        DFS(L+1, sum, tsum+arr[L])

DFS(0, 0, 0)
print(result)
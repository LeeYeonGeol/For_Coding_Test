t = int(input())

k = int(input())

arr = []

ans = 0

for _ in range(k):
    a, b = map(int, input().split())
    arr.append([a, b])


def dfs(start, sum):
    global ans

    if sum > t:
        return
    elif sum == t:
        ans += 1
        return

    for i in range(start, k):
        if arr[i][1] > 0:
            arr[i][1] -= 1
            dfs(i, sum + arr[i][0])
            arr[i][1] += 1

dfs(0,0)
print(ans)


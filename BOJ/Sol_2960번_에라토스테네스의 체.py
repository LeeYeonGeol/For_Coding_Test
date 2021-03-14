n, k = map(int, input().split())

arr = [True] * (n + 1)
arr[0] = [False]
arr[1] = [False]

ans = []
for i in range(2, n + 1):
    if arr[i] == True:
        ans.append(i)
        j = 2
        while(i*j <= n):
            if arr[i*j] == True:
                arr[i*j] = False
                ans.append(i*j)
            j += 1

print(ans[k-1])


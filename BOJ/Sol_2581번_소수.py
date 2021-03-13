import math

m = int(input())
n = int(input())

arr = [True]*(n+1)
arr[0] = False
arr[1] = False
for i in range(2, n+1):
    if arr[i] == True:
        j = 2
        while(i*j <= n):
            arr[i*j] = False
            j += 1

ans = []

for i in range(m, n+1):
    if arr[i] == True:
        ans.append(i)


if not ans:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
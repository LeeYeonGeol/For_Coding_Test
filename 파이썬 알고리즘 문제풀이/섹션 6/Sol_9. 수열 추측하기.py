import sys
import math

n, f = map(int, input().split())

ans = []

sub = [0] * (n)
for i in range(n):
    sub[i] = (math.factorial(n-1)// math.factorial(i)// math.factorial(n-i-1))

def dfs(x, arr):
    if x == n:
        tmp = 0

        for i in range(n):
            tmp += arr[i]*sub[i]

        if tmp == f:
            print(" ".join(list(map(str,arr))))
            sys.exit()
        return
    else:
        for i in range(1, n+1):
            if not i in arr:
                dfs(x+1, arr+[i])

dfs(0, [])
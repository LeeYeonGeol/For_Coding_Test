import sys

n = int(input())

arr = list(map(int, input().split()))

result = 'NO'

total = sum(arr)

def dfs(l, summ):
    if summ>total//2:
        return

    if l == n:
        if summ == total-summ:
            print("YES")
            sys.exit(0)
        return
    else:
        dfs(l+1, summ+arr[l])
        dfs(l+1, summ)

dfs(0, 0)
print(result)
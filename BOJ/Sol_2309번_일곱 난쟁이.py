import sys
arr = []

for _ in range(9):
    arr.append(int(input()))

arr.sort()

def dfs(x, a):
    if x == 2:
        if sum(arr) - sum(a) == 100:
            for i in arr:
                if not i in a:
                    print(i)
            sys.exit()
        return
    else:
        for i in range(9):
            if not arr[i] in a:
                dfs(x+1, a+[arr[i]])

dfs(0, [])
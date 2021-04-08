n, m = map(int, input().split())

cnt = 0

arr = []

def dfs(v):
    global cnt
    if v == m:
        for i in arr:
            print(i, end= " ")
        print()
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            arr.append(i)
            dfs(v+1)
            arr.pop()

dfs(0)
print(cnt)
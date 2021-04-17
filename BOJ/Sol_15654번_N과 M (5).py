n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

check = [False] * (n)
answer = []

def dfs(index):
    if index == m:
        print(" ".join(map(str,answer)))
    else:
        for i in range(n):
            if check[i]:
                continue
            check[i] = True
            answer.append(arr[i])
            dfs(index+1)
            check[i] = False
            answer.pop()

dfs(0)
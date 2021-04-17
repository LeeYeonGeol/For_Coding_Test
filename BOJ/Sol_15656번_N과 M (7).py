n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

answer = []

def dfs(index):
    if index == m:
        print(" ".join(map(str,answer)))
    else:
        for i in range(n):
            answer.append(arr[i])
            dfs(index+1)
            answer.pop()

dfs(0)
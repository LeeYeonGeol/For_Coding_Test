n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

answer = []

def dfs(index, start):
    if index == m:
        print(" ".join(map(str,answer)))
    else:
        for i in range(start, n):
            answer.append(arr[i])
            dfs(index+1, i+1)
            answer.pop()

dfs(0,0)
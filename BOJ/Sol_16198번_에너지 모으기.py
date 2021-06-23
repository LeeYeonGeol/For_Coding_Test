import sys
sys.setrecursionlimit(10**9)

n = int(input())

goosle = list(map(int, input().split()))

ans = []

def dfs(goosle, energy):
    if len(goosle) == 2:
        ans.append(energy)
        return

    for i in range(len(goosle)):
        if i != 0 and i != len(goosle)-1:
            dfs(goosle[:i]+goosle[i+1:] ,energy+goosle[i-1]*goosle[i+1])

dfs(goosle, 0)

print(max(ans))
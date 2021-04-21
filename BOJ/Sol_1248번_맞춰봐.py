import sys
input = sys.stdin.readline

n = int(input())

s = list(input())

cnt = 0

sign = [[0]*n for _ in range(n)]
for a in range(n):
    for b in range(a, n):
        if s[cnt] == '0':
            sign[a][b] = 0
        elif s[cnt] == '+':
            sign[a][b] = 1
        else:
            sign[a][b] = -1
        cnt += 1

ans = []

# 백트래킹
def dfs(level):
    if level >= 1:
        s = 0
        for i in range(level-1,-1,-1):
            s += ans[i]
            if s > 0 and sign[i][level-1] <= 0:
                return
            elif s == 0 and sign[i][level-1] != 0:
                return
            elif s < 0 and sign[i][level-1] >= 0:
                return
    if level == n:
        print(' '.join(map(str,ans)))
        sys.exit()
    for i in range(-10,11):
        ans.append(i)
        dfs(level+1)
        ans.pop()
dfs(0)
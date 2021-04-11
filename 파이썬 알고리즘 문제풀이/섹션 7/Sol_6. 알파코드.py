n = input()

ans = 0

def dfs(L,s):
    global ans
    if L >= len(n):
        print(s)
        ans += 1
        return
    else:
        if n[L] != '0':
            dfs(L+1, s+chr(int(n[L])+64))
        if L+2 <= len(n) and 10 <= int(n[L:L+2]) <= 26:
            dfs(L+2, s+chr(int(n[L]+n[L+1])+64))

dfs(0, "")
print(ans)
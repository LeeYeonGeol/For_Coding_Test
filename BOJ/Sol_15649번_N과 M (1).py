n, m = map(int, input().split())

result = []
def recursive(x, ans = []):

    if len(ans) == m:
        result.append(ans)
        return
    else:
        for i in range(1, x+1):
            if not i in ans:
                recursive(x, ans + [i])

recursive(n)

for r in result:
    for k in range(m):
        print(r[k], end= ' ')
    print()
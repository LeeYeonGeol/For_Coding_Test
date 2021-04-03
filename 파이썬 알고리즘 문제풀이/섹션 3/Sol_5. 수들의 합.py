n, m = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0

s = 0
e = 0
tot = arr[0]
while(e < n):
    if tot == m:
        ans += 1
        tot -= arr[s]
        s += 1
    elif tot < m:
        e += 1
        if e < n:
            tot += arr[e]
    else:
        tot -= arr[s]
        s += 1

for i in range(s,e):
    tot -= arr[i]
    if tot == m:
        ans += 1

print(ans)






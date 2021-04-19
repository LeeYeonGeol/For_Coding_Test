k, n = map(int, input().split())

a = []

for _ in range(k):
    a.append(int(input()))

left = 1
right = max(a)

ans = 0
while (left <= right):
    mid = (left+right)//2
    cnt = 0
    for i in a:
        cnt += i // mid

    if cnt >= n:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)


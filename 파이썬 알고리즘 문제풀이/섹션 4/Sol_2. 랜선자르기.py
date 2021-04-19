k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input()))

left = 1
right = max(arr)
ans = 0
while(left <= right):
    mid = (left+right) // 2
    cnt = 0
    for a in arr:
        cnt += a // mid

    if cnt < n:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)
n, m = map(int, input().split())

arr = list(map(int, input().split()))

left = 1
right = sum(arr)
ans = 0
while(left <= right):
    mid = (left+right)//2

    time = 0
    cnt = 1
    for a in arr:
        if time+a <= mid:
            time += a
        else:
            time = a
            cnt += 1

    if cnt > m:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(ans)



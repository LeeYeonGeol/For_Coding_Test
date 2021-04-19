k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input()))

left = 0
right = max(arr)

result = 0

while(left <= right):
    mid = (left+right) // 2
    result = mid
    cnt = 0
    remain = 0
    for a in arr:
        cnt += (a // mid)
        remain += (a % mid)
    if cnt < n:
        right = mid - 1
    elif cnt > n:
        left = mid + 1
    else:
        if remain <= 0:
            break
        else:
            left += 1


print(result)



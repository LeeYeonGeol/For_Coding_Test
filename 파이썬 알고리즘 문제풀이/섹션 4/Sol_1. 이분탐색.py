n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
left = 0
right = n-1

while(left <= right):
    mid = (left+right) // 2
    if arr[mid] < m:
        left = mid + 1
    elif arr[mid] > m:
        right = mid - 1
    else:
        print(mid+1)
        break

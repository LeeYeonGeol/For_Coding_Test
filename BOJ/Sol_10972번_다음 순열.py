n = int(input())

arr = list(map(int, input().split()))

ans = -1
res = []
for i in range(n-2,-1,-1):
    if arr[i+1] > arr[i]:
        sub = 0
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                sub = j
        arr[i], arr[sub] = arr[sub], arr[i]
        res += arr[:i+1]
        res += arr[i+1:][::-1]


        print(" ".join(map(str, res)))
        break

else:
    print(-1)
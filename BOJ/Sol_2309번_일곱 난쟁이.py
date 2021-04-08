import sys
arr = []

for _ in range(9):
    arr.append(int(input()))

arr.sort()

for i in range(9):
    for j in range(i+1,9):
        if arr[i]+arr[j] == sum(arr)-100:
            for k in range(9):
                if k != i and k != j:
                    print(arr[k])

            sys.exit()
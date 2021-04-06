while(1):
    arr = list(map(int, input().split()))
    k = arr[0]

    if k == 0:
        break

    narr = arr[1:]

    ans = []

    def dfs(x):
        if x == 6:
            for i in ans:
                print(i, end= " ")
            print()
        else:
            for i in range(k):
                if not narr[i] in ans:
                    if ans and ans[-1] > narr[i]:
                        continue
                    ans.append(narr[i])
                    dfs(x+1)
                    ans.pop()
    dfs(0)
    print()
def solution(n, arr1, arr2):
    answer = []
    n_arr = [[0]*n for _ in range(n)]

    for i in range(n):
        val = arr1[i]
        sub = [0]*n
        idx = n-1
        while(val > 0):
            sub[idx] = val%2
            idx -= 1
            val //= 2
        for j in range(n):
            if sub[j] == 1:
                n_arr[i][j] = 1

    for i in range(n):
        val = arr2[i]
        sub = [0]*n
        idx = n-1
        while(val > 0):
            sub[idx] = val%2
            idx -= 1
            val //= 2
        for j in range(n):
            if sub[j] == 1:
                n_arr[i][j] = 1
    for i in n_arr:
        sub = ''
        for j in i:
            if j == 1:
                sub += "#"
            else:
                sub += " "
        answer.append(sub)
    return answer
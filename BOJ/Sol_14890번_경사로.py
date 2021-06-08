n, l = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = 0

def cal4(graph):
    ngraph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ngraph[i][j] = graph[j][n-1-i]
    return ngraph

sub = []

for a in arr:
    sub.append(a)

for a in cal4(arr):
    sub.append(a)


for a in sub:
    # 중복 여부
    gate = []

    tmp = 1
    for i in range(n-1):
        if a[i] == a[i+1]:
            tmp += 1
        else:
            gate.append([a[i], tmp, [False]*tmp])
            tmp = 1
    else:
        if tmp != 0:
            gate.append([a[-1], tmp, [False]*tmp])

    if len(gate) == 1:
        ans += 1
    else:
        # ans가 되는지 여부
        right = True
        for k in range(len(gate)-1):
            if abs(gate[k][0]-gate[k+1][0]) >= 2:
                right = False
                break

            # 앞이 작을 때
            if gate[k][0] < gate[k+1][0]:
                if gate[k][1] < l:
                    right = False
                    break
                else:
                    # 중복 여부 확인
                    if True in gate[k][2][-l:]:
                        right = False
                        break
                    else:
                        for p in range(l):
                            gate[k][2][-p-1] = True
            # 앞이 더 클 때
            else:
                if gate[k+1][1] < l:
                    right = False
                    break
                else:
                    # 중복 여부 확인
                    if True in gate[k+1][2][:l]:
                        right = False
                        break
                    else:
                        for p in range(l):
                            gate[k+1][2][p] = True


        ############################
        if right == True:
            ans += 1

print(ans)
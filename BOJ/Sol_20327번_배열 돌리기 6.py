import sys
input = sys.stdin.readline

# n = , r = 연산 수
n, r = map(int, input().split())

graph = []
for _ in range(2**n):
    graph.append(list(map(int, input().split())))
#graph = [[1,2,3,4,5,6,7,8], [9,10,11,12,13,14,15,16], [17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32],
#[33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48],[49,50,51,52,53,54,55,56],[57,58,59,60,61,62,63,64]]

for _ in range(r):
    k, l = map(int, input().split())

    l2 = 2**l
    a = []
    ngraph = [[0] * (2**n) for _ in range(2**n)]
    # 1번 연산
    if k == 1:
        for i in range(0, 2**n, l2):
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])

                for k in range(len(a)//2):
                    a[k], a[-k-1] = a[-k-1], a[k]

                for x in range(i, i+l2):
                    for y in range(j, j+l2):
                        ngraph[x][y] = a[x-i][y-j]

                a = []
    # 2번 연산
    elif k == 2:
        for i in range(0, 2**n, l2):
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])

                na = []
                for aa in a:
                    na.append(aa[::-1])

                a = []

                for x in range(i, i+l2):
                    for y in range(j, j+l2):
                        ngraph[x][y] = na[x-i][y-j]
    elif k == 3:
        for i in range(0, 2**n, l2):
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])

                na = [[0]*l2 for _ in range(l2)]
                for x in range(l2):
                    for y in range(l2):
                        na[x][y] = a[l2-y-1][x]

                a = []
                for x in range(i, i+l2):
                    for y in range(j, j+l2):
                        ngraph[x][y] = na[x-i][y-j]
    elif k == 4:
        for i in range(0, 2**n, l2):
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])

                na = [[0]*l2 for _ in range(l2)]
                for x in range(l2):
                    for y in range(l2):
                        na[x][y] = a[y][l2-x-1]

                a = []
                for x in range(i, i+l2):
                    for y in range(j, j+l2):
                        ngraph[x][y] = na[x-i][y-j]

    elif k == 5:
        di = dict()
        c = -1
        for i in range(0, 2**n, l2):
            c += 1
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])
                di[(i//l2, j//l2)] = a

                a = []
        for i in range(((2**n)//l2)//2):
            for j in range((2**n)//l2):
                di[(i, j)], di[(c-i,j)] = di[(c-i,j)], di[(i, j)]

        for i in range(((2**n)//l2)):
            for j in range((2**n)//l2):
                aaa = di[(i, j)]
                for a in range(i*l2, i*l2+l2):
                    for b in range(j*l2, j*l2+l2):
                        ngraph[a][b] = aaa[a-(i*l2)][b-(j*l2)]

    elif k == 6:
        di = dict()
        c = -1
        for i in range(0, 2**n, l2):
            c += 1
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])
                di[(i//l2, j//l2)] = a

                a = []

        for i in range(((2**n)//l2)):
            for j in range((2**n)//l2//2):
                di[(i, j)], di[(i,c - j)] = di[(i,c - j)], di[(i, j)]

        for i in range(((2**n)//l2)):
            for j in range((2**n)//l2):
                aaa = di[(i, j)]
                for a in range(i*l2, i*l2+l2):
                    for b in range(j*l2, j*l2+l2):
                        ngraph[a][b] = aaa[a-(i*l2)][b-(j*l2)]

    elif k == 7:
        di = dict()
        c = -1
        for i in range(0, 2**n, l2):
            c += 1
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])
                di[(i//l2, j//l2)] = a

                a = []
        ndi = dict()
        for i in range(((2**n)//l2)):
            for j in range((2**n)//l2):
                ndi[(i, j)] = di[(c - j,i)]

        for i in range(((2**n)//l2)):
            for j in range((2**n)//l2):
                aaa = ndi[(i, j)]
                for a in range(i*l2, i*l2+l2):
                    for b in range(j*l2, j*l2+l2):
                        ngraph[a][b] = aaa[a-(i*l2)][b-(j*l2)]

    elif k == 8:
        di = dict()
        c = -1
        for i in range(0, 2**n, l2):
            c += 1
            for j in range(0, 2**n, l2):
                for g in graph[i:i+l2]:
                    a.append(g[j:j+l2])
                di[(i//l2, j//l2)] = a

                a = []
        ndi = dict()
        for i in range(((2**n)//l2)):
            for j in range((2**n)//l2):
                ndi[(i, j)] = di[(j,c - i)]

        for i in range(((2**n)//l2)):
            for j in range((2**n)//l2):
                aaa = ndi[(i, j)]
                for a in range(i*l2, i*l2+l2):
                    for b in range(j*l2, j*l2+l2):
                        ngraph[a][b] = aaa[a-(i*l2)][b-(j*l2)]
    graph = ngraph

for g in graph:
    print(" ".join(map(str,g)))
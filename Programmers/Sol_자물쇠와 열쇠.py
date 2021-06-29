import copy

def solution(key, lock):
    n = len(key)
    m = len(lock)

    # 회전 함수
    def rotate(key):
        nkey = [[0]*n for _ in range(n)]
        for a in range(n):
            for b in range(n):
                nkey[a][b] = key[n-b-1][a]
        return nkey

    # nlock 만들기
    nlock = [[0] * (2*n+m) for _ in range(2*n+m)]
    for a in range(n, n+m):
        for b in range(n, n+m):
            nlock[a][b] = lock[a-n][b-n]

    # 모든 경우에 대해 check
    for _ in range(4):
        key = rotate(key)
        for a in range(n+m):
            for b in range(n+m):
                nnlock = copy.deepcopy(nlock)
                for i in range(n):
                    for j in range(n):
                        nnlock[a+i][b+j] = key[i][j]^nnlock[a+i][b+j]

                cnt = 0
                for x in range(n, n+m):
                    for y in range(n, n+m):
                        cnt += nnlock[x][y]

                if cnt == m**2:
                    return True

    return False
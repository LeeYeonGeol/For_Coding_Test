import sys

# n = 필드의 수 / z = 타겟 번호 / m = 장애물 수
n, z, m = map(int, input().split())

obstacle = []
if m >= 1:
    obstacle = list(map(int, input().split()))

k = 1
while 1:
    visited = []
    v = 1
    # k에 따라 진행
    while 1:
        v += k

        if v >= n+1:
            v %= n+1
            v += 1
        if not v in visited:
            visited.append(v)
        else:
            break
    for vi in visited:
        if vi in obstacle:
            break
        if vi == z:
            print(k)
            sys.exit()

    k += 1
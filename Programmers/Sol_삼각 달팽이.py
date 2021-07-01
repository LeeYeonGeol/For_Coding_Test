def solution(n):
    answer = []
    triangle = []
    m = []
    for i in range(1, n+1):
        triangle.append([0]*i)
        m.append(i)

    m.sort(reverse=True)

    cnt = 1
    x, y = 0, 0
    case = 0
    for i in range(n):
        # 4 -> 3 -> 2 -> 1
        for j in range(m[i]):
            if case == 0:
                triangle[x][y] = cnt
                cnt += 1
                x += 1
            elif case == 1:
                triangle[x][y] = cnt
                cnt += 1
                y += 1
            elif case == 2:
                triangle[x][y] = cnt
                cnt += 1
                x -= 1
                y -= 1
        if case == 0:
            x -= 1
            y += 1
        elif case == 1:
            y -= 2
            x -= 1
        elif case == 2:
            x += 2
            y += 1
        case += 1
        case = case % 3
    for t in triangle:
        answer += t
    return answer
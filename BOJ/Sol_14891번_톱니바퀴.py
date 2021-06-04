t1 = list(map(int, input()))
t2 = list(map(int, input()))
t3 = list(map(int, input()))
t4 = list(map(int, input()))

# 2, 6이 만나는 지점

k = int(input())

# 0은 N극, 1은 S극 / 다르면 반대 방향으로 회전, 같으면 회전 X

for _ in range(k):
    a, b = map(int, input().split())

    rotate = [0]*5

    if a == 1:
        rotate[a] = b
        while(1):
            if t1[2] == t2[6]:
                break
            else:
                rotate[2] = -rotate[1]
                if t2[2] == t3[6]:
                    break
                else:
                    rotate[3] = -rotate[2]
                    if t3[2] == t4[6]:
                        break
                    else:
                        rotate[4] = -rotate[3]
                        break
    elif a == 2:
        # 1, 2비교
        rotate[a] = b
        if t1[2] != t2[6]:
            rotate[1] = -rotate[2]
        # 2, 3, 4 비교
        while(1):
            if t2[2] == t3[6]:
                break
            else:
                rotate[3] = -rotate[2]
                if t3[2] != t4[6]:
                    rotate[4] = -rotate[3]
                break
    elif a == 3:
        # 1, 2, 3 비교
        rotate[a] = b
        while(1):
            if t2[2] == t3[6]:
                break
            else:
                rotate[2] = -rotate[3]
                if t1[2] == t2[6]:
                    break
                else:
                    rotate[1] = -rotate[2]
                    break
        # 3, 4 비교
        if t3[2] != t4[6]:
            rotate[4] = -rotate[3]
    else:
        rotate[a] = b
        while(1):
            if t3[2] == t4[6]:
                break
            else:
                rotate[3] = -rotate[4]
                if t2[2] == t3[6]:
                    break
                else:
                    rotate[2] = -rotate[3]
                    if t1[2] == t2[6]:
                        break
                    else:
                        rotate[1] = -rotate[2]
                        break

    # rotate 1은 시계 방향 -1은 반시계 방향
    if rotate[1] == 1:
        t1 = [t1[-1]]+ t1[:-1]
    elif rotate[1] == -1:
        t1 = t1[1:]+[t1[0]]

    if rotate[2] == 1:
        t2 = [t2[-1]]+ t2[:-1]
    elif rotate[2] == -1:
        t2 = t2[1:]+[t2[0]]

    if rotate[3] == 1:
        t3 = [t3[-1]]+ t3[:-1]
    elif rotate[3] == -1:
        t3 = t3[1:]+[t3[0]]

    if rotate[4] == 1:
        t4 = [t4[-1]]+ t4[:-1]
    elif rotate[4] == -1:
        t4 = t4[1:]+[t4[0]]

ans = 0

if t1[0] == 1:
    ans += 1

if t2[0] == 1:
    ans += 2

if t3[0] == 1:
    ans += 4

if t4[0] == 1:
    ans += 8

print(ans)
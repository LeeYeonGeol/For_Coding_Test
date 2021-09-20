import sys

input = sys.stdin.readline

r, c = map(int, input().split())


if r == 1 and c == 1:
    print(1)
    sys.exit()
ans = 0

# 오른쪽 -> 아래 -> 왼쪽 -> 아래
dx = [0,1,0,1]
dy = [1,0,-1,0]
# 위 = 0, 아래 = 1, 앞 = 2, 뒤 = 3, 왼 = 4, 오 = 5
jusawi = [1,6,2,5,4,3]

x, y = 0, 0
direction = 0

for i in range(r):
    ans += jusawi[0]
    ans += 14*((c-1)//4)

    for k in range((c-1)%4):
        # 오른쪽, 왼쪽
        if i%2 == 0:
            jusawi[0], jusawi[1], jusawi[4], jusawi[5] = jusawi[4], jusawi[5], jusawi[1], jusawi[0]
        else:
            jusawi[0], jusawi[1], jusawi[4], jusawi[5] = jusawi[5], jusawi[4], jusawi[0], jusawi[1]
        ans += jusawi[0]

    jusawi[0], jusawi[1], jusawi[2], jusawi[3] = jusawi[3], jusawi[2], jusawi[0], jusawi[1]


print(ans)
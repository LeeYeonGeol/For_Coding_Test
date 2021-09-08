from collections import deque
import sys
n = int(input())

bridge = list(map(int, input().split()))

a, b = map(int, input().split())

a -= 1
b -= 1

visited = [-1] * n

# 시작 지점
q = deque()

q.append(a)

visited[a] = 0


# 시작 지점이 정답인 경우
if a == b:
    print(0)
    sys.exit()

while q:
    place = q.popleft()

    sub = []
    jump = bridge[place]

    back, front = place, place
    while 1:
        back -= jump
        if back < 0:
            break

        if visited[back] == -1:
            sub.append(back)
            visited[back] = visited[place]+1
            q.append(back)
    while 1:
        front += jump
        if front >= n:
            break

        if visited[front] == -1:
            sub.append(front)
            visited[front] = visited[place]+1
            q.append(front)

    # 후보에 정답이 있다면
    if b in sub:
        break

print(visited[b])
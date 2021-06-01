from collections import deque
n, k = map(int,input().split())

result = 0
move = deque()
move.append(n)
case = len(move)
visited = [False]*100001
visited[n] = True
last = False

if n == k:
    print(0)
else:
    while(1):
        for _ in range(case):
            x = move.popleft()
            nx = [x-1,x+1,2*x]
            if x-1 == k or x+1 == k or 2*x == k:
                last = True
                continue
            for i in nx:
                if i >= 0 and i <= 100000 and visited[i] == False:
                    visited[i] = True
                    move.append(i)
        result += 1
        case = len(move)
        if last == True:
            break

    print(result)
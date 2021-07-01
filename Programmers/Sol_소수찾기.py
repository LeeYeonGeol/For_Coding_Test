import sys
sys.setrecursionlimit(10**9)

def solution(numbers):
    answer = 0
    tmp = list(numbers)
    li = set()
    visited = [False]*len(tmp)
    def dfs(level, st):
        if st:
            li.add(int(st))
        if level == len(tmp):
            return

        for idx,t in enumerate(tmp):
            if visited[idx] == False:
                visited[idx] = True
                dfs(level+1, st+t)
                visited[idx] = False
    dfs(0,"")

    for l in list(li):
        if l == 0 or l == 1:
            pass
        elif l == 2 or l == 3:
            answer += 1
        else:
            for k in range(2, l-1):
                if l%k == 0:
                    break
            else:
                answer += 1

    return answer
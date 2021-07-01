from collections import defaultdict

def solution(user_id, banned_id):

    answer = []
    dic = defaultdict(list)
    for user in user_id:
        for ban in banned_id:
            if len(user) == len(ban):
                cnt = 0
                for k in range(len(ban)):
                    if user[k] == ban[k]:
                        cnt += 1
                if cnt+ban.count("*") == len(ban):
                    if not user in dic[ban]:
                        dic[ban].append(user)
    tmp = []

    def dfs(level):
        if level == len(banned_id):

            ntmp = sorted(tmp[:])

            answer.append("".join(ntmp))
            return
        for user in dic[banned_id[level]]:
            if not user in tmp:
                tmp.append(user)
                dfs(level+1)
                tmp.pop()

    dfs(0)
    answer = set(answer)

    return len(answer)
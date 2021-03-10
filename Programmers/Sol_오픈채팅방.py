def solution(record):
    id = dict()
    ans = []
    for x in record:
        sub = x.split()
        if sub[0] == 'Enter':
            ans.append([sub[1], '님이 들어왔습니다.'])
            id[sub[1]] = sub[2]
        elif sub[0] == 'Leave':
            ans.append([sub[1], '님이 나갔습니다.'])
        else:
            id[sub[1]] = sub[2]

    result = []
    for x in ans:
        result.append(id[x[0]]+x[1])
    return result

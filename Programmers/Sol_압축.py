def solution(msg):
    answer = []
    db = dict()

    for idx in range(65, 91):
        db[chr(idx)] = idx-64
    last_num = 26

    sub = ""
    idx = 0
    while 1:
        if idx == len(msg):
            break
        sub += msg[idx]

        if not sub in db:
            answer.append(db[sub[:-1]])
            last_num += 1
            db[sub] = last_num
            sub = ""
        else:
            idx += 1
            if idx == len(msg):
                answer.append(db[sub])


    return answer
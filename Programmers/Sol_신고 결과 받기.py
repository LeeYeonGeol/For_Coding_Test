from collections import defaultdict
def solution(id_list, report, k):

    report = list(set(report))
    answer = [0] * len(id_list)

    db_singo = defaultdict(list)
    db_count = defaultdict(int)


    for rep in report:
        a, b = rep.split()
        db_singo[a].append(b)
        db_count[b] += 1

    db_ans = defaultdict(int)
    for db in db_count:
        if db_count[db] >= k:
            for idx, id in enumerate(id_list):
                if db in db_singo[id]:
                    answer[idx] += 1


    return answer
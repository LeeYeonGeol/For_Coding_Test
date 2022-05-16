from collections import defaultdict
def solution(n, t, m, timetable):
    answer = 0

    # n: 셔틀 운행 횟수, t: 셔틀 운행 간격, m: 최대 크루수
    timetable.sort()
    start = 540
    buses = [540]
    for _ in range(n-1):
        start += t
        buses.append(start)

    db = defaultdict(list)

    for time in timetable:
        hour, minute = time.split(":")
        times = int(hour)*60 + int(minute)
        for bus in buses:
            if len(db[bus]) < m and bus >= times:
                db[bus].append(times)
                break

    for bus in buses:
        # 횟수가 남은 경우 -> 버스도착시간 맞춰서
        if len(db[bus]) < m:
            answer = max(answer, bus)
        # 횟수가 안남은 경우
        else:
            answer = max(answer, sorted(db[bus])[-1]-1)


    n_hour, n_minute = str(answer//60), str(answer%60)
    if len(n_hour) == 1:
        n_hour = "0"+n_hour
    if len(n_minute) == 1:
        n_minute = "0"+n_minute

    return n_hour+":"+n_minute
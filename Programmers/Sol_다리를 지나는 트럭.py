from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    index = 0
    bridge = deque()
    for _ in range(bridge_length):
        bridge.append(0)
    check = 0

    weight_check = 0
    while 1:
        if bridge[0] != 0:
            check += 1
            weight_check -= bridge[0]

        bridge.popleft()

        if  index <= len(truck_weights)-1 and weight - weight_check - truck_weights[index] >= 0 :
            bridge.append(truck_weights[index])
            weight_check += truck_weights[index]
            index += 1
        else:
            bridge.append(0)

        answer += 1
        if check == len(truck_weights):
            break

    return answer
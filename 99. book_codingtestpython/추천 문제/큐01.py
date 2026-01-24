# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque()
    answer = 0
    total = 0
    while trucks:
        if total + trucks[0] <= weight:
            candid = trucks[0]
            bridge.append(trucks.popleft())
            total += candid
        else:
            bridge.append(0)

        answer += 1

        if len(bridge) >= bridge_length:
            total -= bridge.popleft()

    return answer + bridge_length

# https://school.programmers.co.kr/learn/courses/30/lessons/150369
# 그리디?


def solution(cap, n, deliveries, pickups):
    answer = 0
    need_d = 0
    need_p = 0

    # 멀리 있는 집부터 수거, 배달 cap 누적
    for i in range(n - 1, -1, -1):
        need_d += deliveries[i]
        need_p += pickups[i]
        while need_d > 0 or need_p > 0:
            answer += 2 * (i + 1)
            need_d -= cap
            need_p -= cap
    return answer

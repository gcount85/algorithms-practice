# 기지국 최소 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/12979


def solution(n, stations, w):
    answer = 0
    location = 1  # 현재 위치
    idx = 0  # 기지국 인덱스

    while location <= n:
        # print(location, idx)

        # 기지국 전파 범위 밖이면
        if (idx <= len(stations) - 1 and location < stations[idx] - w) or idx >= len(
            stations
        ):
            answer += 1
            location += 2 * w + 1

        # 기지국 전파 범위 내부면
        else:
            location = stations[idx] + w + 1
            idx += 1

    return answer

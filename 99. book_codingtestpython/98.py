# https://school.programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict


def solution(gems):
    need = len(set(gems))
    gem_dict = defaultdict(int)
    best = [0, len(gems) - 1]

    start = 0
    for end, gem in enumerate(gems):
        # 종류를 다 모았는지 확인
        gem_dict[gem] += 1
        if len(gem_dict) < need:
            continue

        if end - start + 1 == need:
            return [start + 1, end + 1]

        # 종류를 다 모았으면 최대한 start를 줄여서 best 갱신
        while True:
            # 카운트 제거
            if gem_dict[gems[start]] > 1:
                gem_dict[gems[start]] -= 1
                start += 1
            else:
                break

        # 답 갱신
        min_value = best[1] - best[0]
        now_value = end - start
        if now_value < min_value or (now_value == min_value and start < best[0]):
            best = [start, end]

    return [best[0] + 1, best[1] + 1]

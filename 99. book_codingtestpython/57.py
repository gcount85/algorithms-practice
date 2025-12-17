# https://school.programmers.co.kr/learn/courses/30/lessons/12933


def solution(n):
    n = f"{n}"
    return int("".join(sorted(list(n), reverse=True)))

# https://school.programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations


def solution(n, weak, dist):
    """
    1. weak 배열 => 2배로 늘린다
    2. dist로 순열 뽑음
    3. dist 순열 배열을 순회한다:
        3-1. 늘린 weak 배열에 대해서:
            3-2. 커버해야 하는 부분 정의
    """

    weak_length = len(weak)
    weak2 = weak + [e + n for e in weak]  # [1, 5, 6, 10, 13, 17, 18, 22]
    answer = float("inf")

    for p in permutations(dist):
        for i in range(weak_length):  # 0, 1, 2, 3
            pointer = i
            last_pos = p[0] + weak2[pointer]
            friend = 1
            while pointer < i + weak_length:
                if last_pos >= weak2[pointer]:
                    pointer += 1
                    if pointer == i + weak_length:
                        answer = min(answer, friend)
                        break
                else:
                    friend += 1
                    if friend > len(dist):
                        break
                    last_pos = weak2[pointer] + p[friend - 1]

    return -1 if answer == float("inf") else answer

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

    for p in permutations(dist):  # [1, 2, 3, 4]
        for i in range(weak_length):  # 0, 1, 2, 3
            # 포인터 정의, 첫 친구 보내고 마지막 위치 정의, 사용 친구 개수
            pointer = i
            last_pos = weak2[i] + p[0]  # 2
            friend = 1

            # 1, 5, 6, 10 까지 갈 때까지 (13 미만일때까지)
            while pointer < i + weak_length:
                if last_pos >= weak2[pointer]:
                    pointer += 1
                else:
                    friend += 1
                    if friend > len(p):
                        break
                    last_pos = weak2[pointer] + p[friend - 1]
            else:
                answer = min(answer, friend)

    return -1 if answer == float("inf") else answer

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
            pointer = i  # 포인터 정의
            pos = weak2[pointer] + p[0]  # 친구 거리 + 시작지점 = 첫 마지막위치
            count = 1

            # 포인터를 쫙 밀어라
            while pointer < i + weak_length and count <= len(dist):
                # 취약지점을 커버했으면 포인터를 옮긴다
                if weak2[pointer] <= pos:
                    pointer += 1
                else:
                    if count == len(dist):
                        break
                    count += 1
                    pos = weak2[pointer] + p[count - 1]

            if pointer >= i + weak_length:
                answer = min(answer, count)

    return -1 if answer == float("inf") else answer

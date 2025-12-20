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
    weak2 = weak + [e + n for e in weak]
    answer = float("inf")

    for p in permutations(dist):
        for i in range(weak_length):  # 0, 1, 2, 3
            used = 1

            # ⚠️ 현재 커버해야 할 약점 인덱스 포인터
            j = i

            # 첫 친구가 커버 가능한 끝 위치
            limit = weak2[j] + p[0]

            # 약점 W개를 다 커버할 때까지 진행
            while j < i + weak_length:
                # ⚠️ 현재 친구로 커버 가능한 약점은 전부 PASS => 약점 인덱스 포인터를 쭉 이동시킴
                while j < i + weak_length and weak2[j] <= limit:
                    j += 1

                # 쭉 포인터를 이동했는데 다 커버했으면 성공
                if j >= i + weak_length:
                    answer = min(answer, used)
                    break

                # 아직 약점이 남았는데 친구 더 없으면 실패
                if used >= len(dist):
                    break

                # ⚠️ 다음 친구 투입: "남은 첫 약점"에서 시작
                limit = weak2[j] + p[used]
                used += 1

    return -1 if answer == float("inf") else answer

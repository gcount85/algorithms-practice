# https://school.programmers.co.kr/learn/courses/30/lessons/92342

"""
1. 10점부터 0점까지 반복:
    1-1. 0점인데 remain 남아있거나, remain이 없음:
        0점에 remain몰아줘
        점수 계산해서 max_diff 업뎃
        같은 점수면 더 낮은 점수로 업뎃시켜
    1-1. info[10 - i] + 1개를 라이언 배열에 배분할건데
    1-2. 배분이 안된다(need > remain):
        1-2-1. dfs(remain, 다음 점수, 라이언 배열)
    1-3. 배분된다:
        1-3-1. dfs(remain - need, 다음 점수, 라이언 배열)

"""


def solution(n, info):
    max_diff = 0
    answer = []

    def calculate_score_diff(ryan, apeach):
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if ryan[i] == 0 and apeach[i] == 0:
                continue
            if ryan[i] > apeach[i]:
                ryan_score += 10 - i
            else:
                apeach_score += 10 - i
        return (
            "ryan" if ryan_score > apeach_score else "apeach",
            abs(ryan_score - apeach_score),
        )

    # ⚠️ 이해를 잘 하자
    def better(a, b):
        # 낮은 점수(인덱스 10 -> 0)부터 비교해서
        # 처음으로 다른 곳에서 더 많이 쏜 쪽이 우선
        for i in range(10, -1, -1):
            if a[i] != b[i]:
                return a[i] > b[i]
        return False

    def dfs(remain, score, ryan_array):
        nonlocal answer, max_diff

        if remain == 0 or score == 0:
            ryan_array[10] += remain
            winner, diff = calculate_score_diff(ryan_array, info)
            if winner == "ryan":
                if diff > max_diff:
                    max_diff = diff
                    answer = ryan_array[:]
                elif diff == max_diff:
                    if answer == [] or better(ryan_array, answer):
                        answer = ryan_array[:]

            # ⚠️ 베이스 케이스 특별 처리 원상복구 하고 돌아 가야함
            ryan_array[10] -= remain
            return

        for i in range(score, -1, -1):
            need = info[10 - i] + 1

            if need > remain:
                dfs(remain, i - 1, ryan_array)
            else:
                ryan_array[10 - i] = need
                dfs(remain - need, i - 1, ryan_array)
            ryan_array[10 - i] = 0

    ryan_array = [0 for _ in range(11)]
    dfs(n, 10, ryan_array)
    if max_diff == 0:
        answer.append(-1)

    return answer

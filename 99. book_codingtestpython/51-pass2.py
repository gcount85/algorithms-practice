# https://school.programmers.co.kr/learn/courses/30/lessons/92342

"""
1. 10점부터 0점까지 반복한다.
    E1. 0점 과녁인가요? or remain이 없나요?:
        과녁이 남아있으면 0점칸에 몰빵
        점수 계산해서 max_diff 업뎃
    1-1. need = 어피치가 쏜 거보다 +1발
    1-2. need > remain?:
        1-2-1. 이번 과녁은 포기하고 다음 과녁으로 이동
    1-3. need <= remain?:
        1-3-1. need 만큼 remain에서 제거하고, 화살 배분. 다음에 다음 과녁으로 이동
    1-4. 화살배분 원상복구
"""


def solution(n, info):
    max_diff = 0
    answer = []

    def calculate_score_diff(ryan, apeach):
        ryan_score = 0
        apeach_score = 0
        for i in range(10, -1, -1):  # 10, 9, 8 ... 0
            ryan_count = ryan[10 - i]
            apeach_count = apeach[10 - i]
            if ryan_count == 0 and apeach_count == 0:
                continue
            if ryan_count > apeach_count:
                ryan_score += i
            else:
                apeach_score += i
        return ryan_score - apeach_score

    def better(a, b):
        for i in range(10, -1, -1):  # 10, 9, 8 ... 0
            if a[i] > b[i]:
                return a[:]
            elif a[i] < b[i]:
                return b[:]

    def dfs(remain, target_score, ryan_array):
        nonlocal info, max_diff, answer

        if target_score == 0 or remain == 0:
            ryan_array[10] += remain
            if (
                diff := calculate_score_diff(ryan_array, info)
            ) > 0 and diff >= max_diff:
                # print(diff, ryan_array)
                if max_diff == diff:
                    answer = better(answer, ryan_array)
                else:
                    max_diff = diff
                    answer = ryan_array[:]
            ryan_array[10 - target_score] -= remain
            return

        dfs(remain, target_score - 1, ryan_array)

        need = info[10 - target_score] + 1
        if need <= remain:
            ryan_array[10 - target_score] = need
            dfs(remain - need, target_score - 1, ryan_array)
            ryan_array[10 - target_score] = 0

    ryan_array = [0 for _ in range(11)]
    dfs(n, 10, ryan_array)
    if max_diff == 0:
        answer.append(-1)
    return answer

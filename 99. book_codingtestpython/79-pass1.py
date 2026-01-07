# https://school.programmers.co.kr/learn/courses/30/lessons/12983


def solution(strs, t):
    n = len(t)
    INF = 99999
    dp = [INF] * (n + 1)  # 단어를 i번까지 완성시킬 때 필요한 문자열 조각 최솟값
    sizes = {len(s) for s in strs}
    str_set = set(strs)
    dp[0] = 0

    for i in range(1, n + 1):  # 1, 2, 3, 4, 5, 6
        for L in sizes:  # 1, 2
            if i - L < 0:  # ⚠️ 이거 안 하면 음수 인덱싱 때문에 에러 남
                continue
            if dp[i - L] == INF:
                continue
            back = t[i - L : i]
            if back in str_set:
                dp[i] = min(dp[i], dp[i - L] + 1)
    # print(dp)

    return dp[n] if dp[n] != INF else -1

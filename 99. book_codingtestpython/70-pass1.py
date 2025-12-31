def solution(str1, str2):
    """
    1. 베이스 케이스 계산: 각각 길이가 0일 때, 1일때
    2. 두 문자가 같으면: 이 전 문자까지의 매칭길이 +1
    3. 두 문자가 다르면: 현재문자와 각각 이전문자까지의 매칭 길이 중 max 값
    """

    n = len(str1)
    m = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 두 문자가 같으면
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # 두 문자가 다르면
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp)

    return dp[m][n]


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution("ABCBDAB", "BDCAB"))  # 반환값 : 4
# [       A  B  C  B  D  A  B
#     [0, 0, 0, 0, 0, 0, 0, 0],
#   B [0, 0, 1, 1, 1, 1, 1, 1],
#   D [0, 0, 1, 1, 1, 2, 2, 2],
#   C [0, 0, 1, 2, 2, 2, 2, 2],
#   A [0, 1, 1, 2, 2, 2, 3, 3],
#   B [0, 1, 2, 2, 3, 3, 3, 4],
# ]
print(solution("AGGTAB", "GXTXAYB"))  # 반환값 : 4

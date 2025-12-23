def solution(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution("ABCBDAB", "BDCAB"))  # 반환값 : 4
print(solution("AGGTAB", "GXTXAYB"))  # 반환값 : 4

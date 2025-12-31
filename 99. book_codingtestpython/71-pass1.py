# 오름차순을 유지하면서 길이가 가장 긴 수열


def solution(nums):
    """
    1. nums 길이 * 2 dp 배열 만들고 베이스 케이스 채움
    2. nums 하나씩 순회:
        2-1. 나보다 작은 애들 중에서 dp max 값에 +1
    3. return max(dp)
    """

    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        best = 0
        for j in range(i):
            if nums[j] < nums[i]:
                best = max(best, dp[j])
        dp[i] = 1 + best
    print(dp)
    return max(dp)


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([1, 4, 2, 3, 1, 5, 7, 3]))  # 반환값 : 5
print(solution([3, 2, 1]))  # 반환값 : 1

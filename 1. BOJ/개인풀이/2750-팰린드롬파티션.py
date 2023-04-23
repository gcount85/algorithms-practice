# https://www.acmicpc.net/problem/2705


"""
- dp로 가능할 듯 ! 
- N 파티션 = n//2까지의 1부터 1씩 증가시킨 dp[n]의 누적 합 + 1 (숫자 n 하나 있는 경우)
- 0인 경우도 카운트 해야 할까? -> 안함

"""

import sys

input = sys.stdin.readline
memo = {1: 1, 2: 2, 3: 2}

def solution(n):
    if n in memo:
        return memo[n]
    memo[n] = 1
    for i in range(1, (n//2) + 1):
        memo[n] += solution(i)
    return memo[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))



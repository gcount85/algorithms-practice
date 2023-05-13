# https://www.acmicpc.net/problem/9095

'''
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수
n은 양수이며 11보다 작다.
'''
import sys

memo = {0: 0, 1: 1, 2: 2, 3: 4}
def dp(n):
    if n in memo:
        return memo[n]
    memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
    return memo[n]

input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    n = int(input())
    print(dp(n))



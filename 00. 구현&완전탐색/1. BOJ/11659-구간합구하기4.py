# https://www.acmicpc.net/problem/11659
# refactored 

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
numbers = list(map(int, input().split()))  # 1 <= num <= 1000

# 숫자의 개수만큼 배열 생성
prefix_sum = [0] * (n + 1) 

# 1번부터 n번까지의 누적 합을 차례대로 구한다 
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + numbers[i]

# i ~ j까지의 누적 합은 j까지의 누적 합에서 i까지의 누적 합을 뺀 값
def range_sum(i, j):
    return prefix_sum[j + 1] - prefix_sum[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(range_sum(i - 1, j - 1))

# 메모리 초과
# memo = {}

# def dp(i, j):
#     if (i, j) in memo:
#         return memo[(i, j)]
#     if i == j:
#         return numbers[i]
#     if i > j:
#         return 0
#     memo[(i, j)] = dp(i, j-1) + numbers[j]
#     return memo[(i, j)]

# for _ in range(m):
#     i, j = map(int, input().split())
#     print(dp(i-1, j-1))





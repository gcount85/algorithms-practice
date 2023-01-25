# https://www.acmicpc.net/problem/1074
"""
크기가 2N * 2N인 2차원 배열을 Z모양으로 탐색
N > 1인 경우, 배열을 크기가 2^N-1 * 2^N-1로 4등분 한 후에 재귀적으로 순서대로 방문
N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력
정수 N, r(행), c(열)
1 ≤ N ≤ 15
0 ≤ r, c < 2^N

"""


import sys
input = sys.stdin.readline


def Z(N, r, c, count):
    if (N == 0):
        return count
    else:
        smaller_quad = (2**(N-1))
        if (r < smaller_quad) and (c < smaller_quad):  # 제1분면
            return Z(N-1, r, c, count)
        elif (r < smaller_quad) and (c >= smaller_quad):  # 제2분면
            count += (2**(2*N-2))
            return Z(N-1, r, c-smaller_quad, count)
        elif (r >= smaller_quad) and (c < smaller_quad):  # 제3분면
            count += (2 * (2**(2*N-2)))
            return Z(N-1, r-smaller_quad, c, count)
        elif (r >= smaller_quad) and (c >= smaller_quad):  # 제4분면
            count += (3 * (2**(2*N-2)))
            return Z(N-1, r-smaller_quad, c-smaller_quad, count)


N, r, c = map(int, input().split())
print(Z(N, r, c, 0))


# 1. 재귀 브레이크 (2^0 * 2^0 크기의 배열에 도착했을 때)
# 2. 1,2,3,4 분면 중 어디에 속하는지 판별 → 제일 작은 Z에 도달할 때까지
# 3. count 계산 (1분면 +0, 2분면 +1 ... )

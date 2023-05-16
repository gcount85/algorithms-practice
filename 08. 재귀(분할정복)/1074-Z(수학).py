# https://www.acmicpc.net/problem/1074

# 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력
# 정수 N, r(행), c(열)
# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2^N


import sys


def z(N, r, c):
    if (N == 0):
        return 0

    return 2*(r % 2)+(c % 2) + 4*z(N-1, int(r/2), int(c/2))


N, r, c = map(int, sys.stdin.readline().split())

print(z(N, r, c))

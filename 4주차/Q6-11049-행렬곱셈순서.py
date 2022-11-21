# https://www.acmicpc.net/problem/11049

import sys

N = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    matrix.append((r, c))

DP = [[0] * ]  # 히히히 화이팅 
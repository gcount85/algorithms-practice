# https://www.acmicpc.net/problem/18870

"""
N개의 좌표 X1, X2, ..., XN

"""
import sys

n = int(sys.stdin.readline())
# refactored
coords = list(map(int, input().split()))
co_count = {}  # 좌표의 개수를 담은 딕셔너리
count = 0  # 임의의 좌표 c 보다 작은 좌표의 개수
for c in sorted(coords):
    if c not in co_count:
        co_count[c] = count
        count += 1
print(*[co_count[x] for x in coords])

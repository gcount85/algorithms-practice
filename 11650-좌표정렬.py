import sys

input = sys.stdin.readline

N = int(input())
coordinates = [tuple(map(int, input().split(' '))) for _ in range(N)]
coordinates.sort()
for a, b in coordinates:
    print(a, b)

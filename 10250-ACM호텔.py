# https://www.acmicpc.net/problem/10250

import sys


T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    층 = N % H   # 10 % 6
    호 = N // H  # 10 // 6
    if (층 != 0):
        호 += 1
    if (층 == 0):
        층 = 6
    if 호 < 10:
        호 = "0" + str(호)
    print(str(층)+str(호))

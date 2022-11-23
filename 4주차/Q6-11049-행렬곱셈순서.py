# https://www.acmicpc.net/problem/11049

import sys

N = int(sys.stdin.readline())
M = [0]
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    M.append((r, c))

# print(M)

DP = [[0] * (N+1) for _ in range(N+1)]  

itvl = 1
for _ in range(N-1):
    for i in range(1, N+1):
        j = i + itvl
        if j < N+1:
            DP[i][j] = min(DP[i][j-1] + (M[i][0] * M[j][0] * M[j][1]),
                           DP[i+1][j] + (M[i][0] * M[j-1][0] * M[j][1]))
    itvl += 1

print(DP[1][N])

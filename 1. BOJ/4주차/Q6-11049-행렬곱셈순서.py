# https://www.acmicpc.net/problem/11049

import sys

# 입력받기; M = [0, P1, P2, P3 ... ]
N = int(sys.stdin.readline())
M = [0]
for i in range(N):
    r, c = map(int, sys.stdin.readline().split())
    if i == 0:
        M.extend([r, c])
    else:
        M.extend([c])

# print(M)

# 이차원 DP 테이블
DP = [[0] * (N+1) for _ in range(N+1)]

# DP 테이블에서 '↘' 이런 대각선 방향으로 채워나가야 하기 때문에 인덱스 인터벌을 만듦
itvl = 1
for _ in range(N-1):
    for i in range(1, N):
        j = i + itvl
        if j < N+1:  # 인덱스 에러 안 나게 j의 인덱스 제한
            min = 2**31
            # DP[i][j]는 k를 i부터 j-1까지 증가시키면서
            # DP[i][k] + DP[k+1][j] + M[i]*M[K+1]*M[j+1](두 행렬의 곱셈 비용)의 최소값이다
            for k in range(i, j):
                temp = DP[i][k] + DP[k+1][j] + (M[i]*M[k+1]*M[j+1])
                if temp < min:
                    min = temp
            DP[i][j] = min
    itvl += 1

print(DP[1][N])

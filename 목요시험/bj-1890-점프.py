# https://www.acmicpc.net/problem/1890 점프

# 답이 정답이랑 다르게 나와요 

import sys

N = int(sys.stdin.readline())

board = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)
# print(board)

dp = [[0] * (N+1) for _ in range(N+1)]

# print(dp)
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == 1 and j == 1:
            dp[i][j] += 1
        itvl = board[i-1][j-1]
        if (j+itvl < N+1):
            dp[i][j+itvl] += 1        
        if (i+itvl < N+1): 
            dp[i+itvl][j] += 1        

print(dp)

'''
dp[1->마지막칸] = dp[1->마지막칸왼쪽줄(3,2,1일때)] + dp[1->마지막칸윗줄(3,2,1일때)] 

'''
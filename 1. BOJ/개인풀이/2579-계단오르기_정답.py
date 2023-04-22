import sys

input = sys.stdin.readline

N = int(input())
score = [0] + [int(input()) for _ in range(N)]
memo = [0] * (N+1)

memo[1] = score[1]
if N >= 2:
    memo[2] = score[1] + score[2]

for i in range(3, N+1):
    memo[i] = max(memo[i-2] + score[i],
                  memo[i-3] + score[i-1] + score[i])  # 두 가지 경우만 고려

print(memo[N])

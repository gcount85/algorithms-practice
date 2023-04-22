
import sys

input = sys.stdin.readline


N = int(input())
score = [0]+[int(input().strip()) for _ in range(N)]
# print(score)
memo = {N: (score[N], 1), N-1: (score[N-1]+score[N], 2)}  # 연속적으로 싱글 스텝을 밟은 카운트


for stair in range(N-2, -1, -1):
    if (memo[stair+1][1] == 2) and (stair != 0):  # 세 계단 연속 밟게 된다면
        memo[stair] = (memo[stair+2][0] + score[stair], 1)
    else:
        if memo[stair+1][0] >= memo[stair+2][0]:
            memo[stair] = (memo[stair+1][0] + score[stair], memo[stair+1][1]+1)
        else:
            memo[stair] = (memo[stair+2][0] + score[stair], 1)


# print(max(memo[1][0], memo[2][0]))
print(max(memo[0][0], memo[1][0], memo[2][0]))
print(memo)

"""
반례1
10
100
100
1
1
100
100
1
1000
1000
1000

답: 2302


5
50
40
30
20
10

출력 : 90
정답 : 120
(50 40 20 10)

"""

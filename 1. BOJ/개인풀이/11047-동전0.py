# https://www.acmicpc.net/problem/11047

import sys

count, won = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(count)]

# print(coins)

answer = 0
for value in coins[::-1]:
    if (won == 0):
        break
    if (value > won):
        continue
    answer += (won // value)
    won = (won % value)

print(answer)


"""
1. 제일 큰 가치부터 계산
2. 들어간 동전 수 업데이트
3. 남은 금액 업데이트
4. 위 과정 반복

"""

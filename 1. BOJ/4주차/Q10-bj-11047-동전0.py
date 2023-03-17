# https://www.acmicpc.net/problem/11047

import sys

N, K = map(int, sys.stdin.readline().split())  #  (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
A = [int(sys.stdin.readline()) for _ in range(N)]  #  (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

count = 0
for i in A[::-1]: 
    if i > K:
        continue
    else:
        count += K // i
        K = K % i
    if K == 0:
        break
print(count)




'''
가장 큰 가치의 돈으로 먼저 계산하고 카운트
잔액이 0이 될 때까지 반복
    잔액을 그 다음 가치의 돈으로 계산하고 카운트
'''



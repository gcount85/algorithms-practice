# https://www.acmicpc.net/problem/9020
####
# 골드바흐의 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있음 -> 골드바흐의 수 
# 골드바흐 파티션: 두 짝수를 두 소수의 합으로 나타낸 것
####
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
####

import sys

sieve = [True] * 10000
# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
min = 9998
m = int(100000 ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:           # i가 소수인 경우
        for j in range(i+i, 10000, i): # i이후 i의 배수들을 False 판정
            sieve[j] = False

# print(sosu)
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    answer = None
    for i, v in enumerate(sieve[2:n+1]):
        for j, k in enumerate(sieve[2:n+1]):
            if v == False or k == False:
                continue
            if i > j:
                continue
            if i + j != n:
                continue
            if i - j == 0:
                answer = (i, i)
                break
            if i - j < min:
                min = i - j
                answer = (i, j)
    print(answer[0], answer[1])





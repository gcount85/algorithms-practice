# https://www.acmicpc.net/problem/9020
# 골드바흐의 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있음 -> 골드바흐의 수 
# 골드바흐 파티션: 두 짝수를 두 소수의 합으로 나타낸 것
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

import sys

sieve = [True] * 10000
# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
m = int(100000 ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:           # i가 소수인 경우
        for j in range(i+i, 10000, i): # i이후 i의 배수들은 소수가 아니므로 False 판정
            sieve[j] = False

T = int(sys.stdin.readline()) 
for _ in range(T):
    n = int(sys.stdin.readline())
    mid = n // 2     # 탐색을 위한 중간값 지정
    # 소수 리스트를 검색하기 위한 인덱스 a, b로, a는 1씩 감소, b는 1씩 증가시켜 가장 차이가 적은 값부터 찾게 됨
    a, b = mid, mid  
    for _ in range(mid):
        if (sieve[a] and sieve[b]) and (a + b == n):  # 소수이고 합이 답과 같은 경우
            print(a, b)   
            break
        else:
            a -= 1
            b += 1
        








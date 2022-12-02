# https://www.acmicpc.net/problem/9020
####
# 골드바흐의 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있음 -> 골드바흐의 수 
# 골드바흐 파티션: 두 짝수를 두 소수의 합으로 나타낸 것
####
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
####

import sys

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]



T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    sosu = [2, 3]
    # sosu = [num for num in range(3, n, 2) for i in range(2, int(math.sqrt(num))+1) if num % i != 0]
    for num in range(5, n, 2):
        count = 0
        if num % 9 == 0:
            continue
        for i in range(2, int(num**0.5)+1):
            if num % i == 0: 
                count += 1
        if count == 0:
            sosu.append(num)
    min = 9998
    answer = None
    for i in sosu[::-1]:
        for j in sosu[::-1]:
            if i+j != n:
                continue
            if i - j == 0:
                answer = (j, i)
                break
            if (i > j) and (i - j < min):
                min = i - j
                answer = (j, i)
    print(answer[0], answer[1])





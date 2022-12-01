# https://www.acmicpc.net/problem/9020
####
# 골드바흐의 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있음 -> 골드바흐의 수 
# 골드바흐 파티션: 두 짝수를 두 소수의 합으로 나타낸 것
####
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
####

import sys, math

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    sosu = [num for num in range(2, n) for i in range(2, int(math.sqrt(num))+1) if num % i != 0]
    for num in range(2, n):
        count = 0
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0: 
                count += 1
        if count == 0:
            sosu.append(num)
    min = 9998
    answer = None
    for i in sosu[::-1]:
        for j in sosu[::-1]:
            if i < j:
                continue
            if i+j != n:
                continue
            if i - j < min:
                min = i - j
                answer = (j, i)

            

    # comb = itertools.combinations(sosu, 2)
    # for i in comb:

    print(answer[0], answer[1])





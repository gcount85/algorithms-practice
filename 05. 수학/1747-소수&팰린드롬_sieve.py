"""
- n보다 같거나 큼, 소수이면서 팰린드롬, 가장 작은 수 
- 1 <= n <= 1000000

- 백만 다음의 가장 작은 소수까지 체로 구하고 팰린드롬 판별하기

"""


import sys, math

input = sys.stdin.readline

n = int(input())
bound = 1003002
sieve = [1] * bound
sieve[0] = sieve[1] = 0

# 배수에 해당하는 숫자는 False로 바꿈
for i in range(2, round(math.sqrt(bound))+1):
    if sieve[i] == 1:
        # for j in range(2, round(math.sqrt(bound))+1):
        for j in range(i * i, bound, i): # i의 제곱부터 배수를 걸러냄
            sieve[j] = 0

# n보다 같거나 큰 소수들 중 팰린드롬 여부 확인
for k in range(n, bound):
    if sieve[k] == 1:
        candid = str(k)
        s, e = 0, len(candid)-1
        isPalindrome = 1
        while s < e:
            if candid[s] != candid[e]:
                isPalindrome = 0
                break
            s += 1
            e -= 1
        if isPalindrome:
            print(k)
            break


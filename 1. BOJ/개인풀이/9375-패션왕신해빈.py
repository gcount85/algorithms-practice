import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        apparel, type = input().strip().split()
        if type not in clothes:
            clothes[type] = 1
        else:
            clothes[type] += 1
    # print(clothes)

    comb = 1
    for v in clothes.values():
        comb *= v + 1

    print(comb-1)

'''
프로그래머스의 "위장"과 비슷한 문제!

'''

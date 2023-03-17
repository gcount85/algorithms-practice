# https://www.acmicpc.net/problem/9084

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    # 경우의 수를 담은 DP 테이블 
    table = dict.fromkeys(range(1,M+1), 0)

    # 돈의 가치에 따라 경우의 수 계산하기 → 동전의 가치가 작은 순으로 경우의 수를 구하지 않으면 답이 나오지 않음! 
    for k in table.keys():   
        if coins[0] <= k < coins[1]:  # 1<k<5
            table[k] = 1
        elif coins[1] < k < coins[2]:
            table[k] = 2
        elif coins[2] == k:
            table[k] = 3
        elif k > coins[2]:
            table[k] = table[k-coins[0]] + table[k-coins[1]] + table[k-coins[2]]
        # print(f"동전이 {c}원일 때, 돈이 {k}원일 때, 경우의수 {table}")
        print(f"돈이 {k}원일 때")
                
    print(table[M])







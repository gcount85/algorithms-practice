# https://www.acmicpc.net/problem/9084

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    # 경우의 수를 담은 DP 테이블 
    table = dict.fromkeys(range(1,M+1), 0)

    # 돈의 가치에 따라 경우의 수 계산하기
    for c in coins:       
        for k in table.keys():   
            if k == c:          # 동전과 돈의 가치가 같을때, 경우의 수는 하나밖에 없음
                table[k] += 1
            elif k > c:         # 돈의 가치가 동전의 가치보다 클 때, 동전의 가치만큼 뺀 값의 경우의 수를 더함
                table[k] += table[k-c] 
    print(table[M])






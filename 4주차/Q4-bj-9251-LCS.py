# https://www.acmicpc.net/problem/9251

import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()


LCS = [[0] * (len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:    # A와 B의 끝 문자가 같으면 이전의 LCS에서 +1
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:                   # A와 B의 끝 문자가 다른 경우 DP 테이블에서 위칸, 왼쪽칸의 값 중 max
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
        
print(LCS[-1][-1]) 
 

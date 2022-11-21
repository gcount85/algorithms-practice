# https://www.acmicpc.net/problem/9251

import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

# ACAYKP
# CAPCA

LCS = dict.fromkeys(range(len(A)),None)  # key; 0 ~ 5

for i in LCS.keys():
    if i == 0:
        if A[0] == B[0]:
            LCS[0] = (B[0], 1)
        else:
            LCS[0] = ("", 0)
    elif B[i] in A[LCS[i-1][1]:i+1]:
        LCS[i] = (LCS[i-1][0] + B[i], A[LCS[i-1][1]:i+1].index(B[i])+1)
    else: 
        LCS[i] = LCS[i-1]
        
print(len(LCS[len(A)-1][0]))
# print(LCS[len(A)-1])


import sys
from itertools import permutations

def 절대값더하기(i, 조합):
    if i == 0:
        return 0
    else:
        return 절대값더하기(i-1, 조합) + abs(조합[i-1]-조합[i])

N = int(sys.stdin.readline()) # 3 <= N <= 8   
A = list(map(int, sys.stdin.readline().split()))
# N = 6   
# A = [20, 1, 15, 8, 4, 10]
합목록 = [절대값더하기(N-1, i) for i in permutations(A)]
print(max(합목록))


## 순열 조합 함수 있다고 함 !! 
    
        





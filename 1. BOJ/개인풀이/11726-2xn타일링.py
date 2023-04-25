import sys

input = sys.stdin.readline
n = int(input())

# n-1의 경우의 수 + n-2일때 경우의 수
memo = {1: 1, 2: 2, 3: 3} 
def tiling(n):
    if n in memo:
        return memo[n]
    memo[n] = (tiling(n-1) + tiling(n-2)) % 10007  
    return memo[n]
    
print(tiling(n))

# https://www.acmicpc.net/problem/1629

# 자연수 A를 B번 곱한 수를 알고 싶다. 
# 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. 
# A, B, C는 모두 2,147,483,647 이하의 자연수이다.

# 출력
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

import sys
sys.setrecursionlimit(10**6)
A, B, C = 10, 11, 12
# A, B, C = map(int, sys.stdin.readline().split())
# a = ((A % C) * ((A**(B-3)) % C)) % C
# t = ((A % C) * (a) % C)
# ans = ((A % C) * (t) % C)

# x = A**B-1
# (A * x) = ((A % C) * (x % C)) % C

def div(A, B, C):
    if B == 1:
        return 1
    else:
        ans = ((A**(B/2) % C) * ((div(A, B-1, C))**B/2) % C) % C
        return ans

print(div(A, B, C))







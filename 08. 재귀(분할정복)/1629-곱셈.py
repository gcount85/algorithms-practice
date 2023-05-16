# https://www.acmicpc.net/problem/1629

from sys import stdin

a, b, c = map(int, stdin.readline().split())

def pow(a, b):
    # a^1에 도달한 경우 
    if b == 1:  
        return a % c

    tmp = pow(a, b//2)
    # 지수가 짝수인 경우 
    if b % 2 == 0:   
        return tmp * tmp % c
    # 지수가 홀수인 경우
    return tmp * tmp * a % c        
    

print(pow(a, b))


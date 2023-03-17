# https://www.acmicpc.net/problem/2078

import sys

L, R = map(int, sys.stdin.readline())
# 루트는 (1,1) 
# 어떤 노드가 (a, b)가 할당되었을 때, 
# 그 노드의 왼쪽 자식에는 (a+b, b)가 할당되고, 오른쪽 자식에는 (a, a+b)가 할당됨
# 왼쪽 자식은 b가 동일하고 오른쪽 자식은 a가 동일함 

root = (1, 1)


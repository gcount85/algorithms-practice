# https://www.acmicpc.net/problem/17219

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
for _ in range(N):
    url, pwd = input().strip().split()
    dict[url] = pwd
for _ in range(M):
    print(dict[input().strip()])

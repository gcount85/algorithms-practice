# https://www.acmicpc.net/problem/10989
# 도수 정렬(counting sort)

"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)
둘째 줄부터 N개의 줄에는 수
수는 10,000보다 작거나 같은 자연수

"""

import sys
input = sys.stdin.readline

횟수 = int(input())
배열 = [0] * 10001

# 수 입력받기 + 배열에 counting
for i in range(횟수):
    숫자 = int(input())
    배열[숫자] += 1

# 배열의 count 수만큼 인덱스 출력
for i in range(10001):
    if (배열[i] != 0):
        for _ in range(배열[i]):
            print(i)

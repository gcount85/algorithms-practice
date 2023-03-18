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

N = int(input())
array = [0] * 10001

# 수 입력 + 배열에 count
for i in range(N):
    num = int(input())
    array[num] += 1

# 배열을 순회하며 count가 존재하면 인덱스 출력
for j in range(1, 10001):
    if (array[j] != 0):
        for _ in range(array[j]):
            print(j)

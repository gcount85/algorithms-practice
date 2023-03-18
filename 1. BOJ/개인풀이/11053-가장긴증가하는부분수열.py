# https://www.acmicpc.net/problem/11053

"""
수열 A의 가장 긴 증가하는 부분 수열을 구하라

- 입력
첫째 줄에 수열 A의 크기 (1 ≤ N ≤ 1,000)
둘째 줄에 수열 A를 이루고 있는 A의 원소들 (1 ≤ Ai ≤ 1,000)

- 출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이 출력

"""

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
LIS = [A[0]]

# todo: m이 -1이 뜰 때 해결


def binary_search(l, h, target):
    m = (l+h)//2
    if h >= l:
        if (target == LIS[m]) or (l >= h and target < LIS[m]):
            return m
        if l >= h and target > LIS[m]:
            return m+1
        if target < LIS[m]:
            return binary_search(l, m-1, target)
        if target > LIS[m]:
            return binary_search(m+1, h, target)


for i in range(1, N):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    elif A[i] < LIS[-1]:  # 이분탐색으로 들어갈 자리 찾아서 대체
        index = binary_search(0, len(LIS)-1, A[i])
        LIS[index] = A[i]

print(len(LIS))


"""
1. A의 원소들에 대해 반복 -> A[i]를 배열 LIS에 배치
    1) LIS의 마지막 원소보다 A[i]가 크다면: LIS에 A[i] 추가
    2) 작다면:
        1) 배열 LIS안에 A[i]가 오름차순으로 위치할 수 있는 곳 이분탐색
        2) 이분탐색으로 찾은 LIS의 해당 자리 값을 A[i]의 값으로 대체
2. 배열 LIS의 길이 -> 정답

"""

"""
반례
20
31 84 18 62 35 77 23 53 60 94 3 77 60 51 42 18 83 85 63 51
답 7

8
10 15 20 1 2 3 4 5
답 5

6
1 5 2 6 3 4
답 4

5
3 1 3 2 1  
정답: 2

5
1 2 1 2 3
3

4
1 4 2 3
답 3

5
1 4 2 3 5
답 4




"""

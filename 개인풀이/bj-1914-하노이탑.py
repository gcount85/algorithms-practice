# https://www.acmicpc.net/problem/1914

"""
세 개의 장대
첫 번째 장대에는 반경이 서로 다른 N개의 원판이 있음 
각 원판은 반경이 큰 순서대로 쌓여있다. 
다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮긴다. 
    1. 한 번에 한 개의 원판만 다른 탑으로 옮김
    2. 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 함
이 작업을 수행하는데 필요한 이동 순서를 출력
단, 이동 횟수 K는 최소

입력: 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)
출력
- 첫째 줄에 옮긴 횟수 K
- N이 20 이하인 입력에 대해서만, 둘째 줄부터 빈칸을 사이에 두고 A, B를 출력
- 두 정수 A B는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻

"""

import sys

input = sys.stdin.readline
inputN = int(input())
count = 0


def hanoi(N: int, A: int, B: int):
    global count, inputN

    if (N == 0):
        return

    count += 1
    if (inputN <= 20):
        print(A, B)

    hanoi(N-1, A, 2)
    # hanoi(N-2, A, B)
    hanoi(N-1, 2, B)  # 마지막 공통 단계


hanoi(N=inputN, A=1, B=3)
print(count)

"""

"""

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

maxlen = 0
for i in range(N):
    s = i
    e = i+1
    count = 0
    last = A[e-1]
    while (e < N-1):
        if (A[e] > last):
            if count == 0:
                count += 2
            else:
                count += 1
        e += 1
    maxlen = max(count, maxlen)
print(maxlen)


"""
1. s, e 인덱스에서 검색 시작 (count = 0)
2. e+1 인덱스 값 확인 
    1) list[e] 값보다 큰 경우, count + 1
    2) list[e] 값보다 작은 경우, s = e+1로 다시 위 과정 반복 
3. 인덱스가 리스트의 마지막에 도달하면 반복 종료

반례

5
3 1 3 2 1  
정답: 2

5
1 2 1 2 3
3

"""

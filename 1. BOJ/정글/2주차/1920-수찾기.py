# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)
# 다음 줄에 N개의 정수 A[1], A[2], …, A[N]
# 다음 줄에 M(1 ≤ M ≤ 100,000)
# 다음 줄에 M개의 수
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys

# 이분 탐색 재귀 함수
def bi_search(num, lst, low, high):
    if (low > high):  # low가 high보다 커지는 상황은 숫자가 없어서 인덱스가 역전되는 것 
        return 0
    else:
        mid = (low + high) // 2
        if (num == lst[mid]):
            return 1
        elif (num < lst[mid]):
            return bi_search(num, lst, low, mid-1)
        else:
            return bi_search(num, lst, mid+1, high)

# 입력받기
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
# print(N, N_list, M, M_list)

# 입력 예시
# N = 5
# N_list = [4, 1, 5, 2, 3]
# M = 5
# M_list = [1, 3, 7, 9, 5]

N_list.sort()

# M리스트의 숫자에 대해서 이분 탐색
for num in M_list:
    print(bi_search(num, N_list, 0, N-1))




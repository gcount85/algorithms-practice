# https://www.acmicpc.net/problem/2110


import sys
import numpy as np
from itertools import combinations

집의개수N = 5
공유기개수C = 3   #
집좌표 = [1, 2, 4, 8, 9]

집좌표.sort()

# 공유기경우의수 = combinations(집좌표, 공유기개수C)


def search(list, 공유기개수C, low, high):  # 인덱스로 안함당
    global 집좌표
    if (low > high):  # low가 high보다 커지는 상황은 값이 없어서 인덱스가 역전되는 것
        return False
    else:
        mid = (low + high) // 2
        H = sum([i-H_range[mid] for i in height_lst if i > H_range[mid]])
        # print(H)
        if H == M:
            return H_range[mid]
        elif H < M:
            return find_H(M, H_range, low, mid-1)
        else:
            return find_H(M, H_range, mid+1, high)

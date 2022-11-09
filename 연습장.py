# https://www.acmicpc.net/problem/1920

import sys

def bin_search(arr, src):
    pl = 0
    pr = len(arr) - 1

    while True:
        pc = (pl + pr) // 2

        if arr[pc] == src:
            return "1"
        elif arr[pc] < src:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            break
    return "0"

print_list = ""

count = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

src_count = int(sys.stdin.readline())
src_num = list(map(int, sys.stdin.readline().split()))

num.sort()
for i in src_num:
    print_list += bin_search(num,i)

for i in range(len(print_list)):
    print(print_list[i])
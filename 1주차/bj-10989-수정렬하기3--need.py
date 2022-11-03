# counting sort!

import sys

횟수 = int(sys.stdin.readline())
배열 = [0] * 10001

for i in range(횟수):
    숫자 = int(sys.stdin.readline())
    배열[숫자] += 1

for i in range(10001):
    if 배열[i] != 0:
        for j in range(배열[i]):
            print(i)



    

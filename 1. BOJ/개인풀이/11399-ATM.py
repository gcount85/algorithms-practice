# https://www.acmicpc.net/problem/11399

import sys
import functools

# reduce 이용
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().strip().split()))
time.sort()

answer = [time[0]]


def calculate(x, y):
    answer.append(x+y)
    return x+y


functools.reduce(calculate, time)

print(sum(answer))


# while loop 이용 (더 빠름)
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().strip().split()))
time.sort()

total_waiting_time = 0
current_waiting_time = 0

for t in time:
    current_waiting_time += t
    total_waiting_time += current_waiting_time

print(total_waiting_time)

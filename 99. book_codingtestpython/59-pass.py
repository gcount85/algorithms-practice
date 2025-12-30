# https://school.programmers.co.kr/learn/courses/30/lessons/42746#

from functools import cmp_to_key


def cmp(a, b):
    int1 = int(str(a) + str(b))
    int2 = int(str(b) + str(a))
    if int1 > int2:
        return 1
    else:
        return -1


def solution(numbers):
    numbers.sort(key=cmp_to_key(cmp), reverse=True)
    number = "".join(list(map(str, numbers)))
    return "0" if int(number) == 0 else number

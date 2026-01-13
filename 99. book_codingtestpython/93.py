# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# 스택으로 초기 풀었다가 내장함수 이용하는 걸로 바꿈.


def to_k_base(n: int, k: int):
    if n == 0:
        return "0"
    digits = ""
    while n:
        digits = str(n % k) + digits
        n //= k
    return digits


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def solution(n, k):
    """
    1. n을 k진수로 바꿈
    2. 하나씩 스택에 추가하면서 패턴에 맞는거 있는지 확인
    """

    k_base_num = to_k_base(n, k)
    count = 0
    k_base_num = k_base_num.split("0")
    for elem in k_base_num:
        if elem and is_prime(int(elem)):
            count += 1
    return count
